import math


class DeepRacer:
    MAX_SPEED = float(5.0)
    MIN_SPEED = float(1.5)
    MAX_STEERING_ANGLE = 30
    SMOOTH_STEERING_ANGLE_TRESHOLD = 15
    SAFE_HORIZON_DISTANCE = 0.8
    CENTERLINE_FOLLOW_RATIO_TRESHOLD = 0.12
    ANGLE_IS_CURVE = 3
    PENALTY_MAX = 0.001
    REWARD_MAX = 100000

    params = None
    all_wheels_on_track = None
    x = None
    y = None
    distance_from_center = None
    is_left_of_center = None
    is_reversed = None
    heading = None
    progress = None
    steps = None
    speed = None
    steering_angle = None
    track_width = None
    waypoints = None
    closest_waypoints = None
    nearest_previous_waypoint_ind = None
    nearest_next_waypoint_ind = None

    def init_self(self, params):
        self.all_wheels_on_track = params['all_wheels_on_track']
        self.x = params['x']
        self.y = params['y']
        self.distance_from_center = params['distance_from_center']
        self.is_left_of_center = params['is_left_of_center']
        self.is_reversed = params['is_reversed']
        self.heading = params['heading']
        self.progress = params['progress']
        self.steps = params['steps']
        self.speed = params['speed']
        self.steering_angle = params['steering_angle']
        self.track_width = params['track_width']
        self.waypoints = params['waypoints']
        self.closest_waypoints = params['closest_waypoints']
        self.nearest_previous_waypoint_ind = params['closest_waypoints'][0]
        self.nearest_next_waypoint_ind = params['closest_waypoints'][1]

    def __init__(self, params):
        self.params = params
        self.init_self(params)

    def get_way_point(self, index_way_point):
        if index_way_point > (len(self.waypoints) - 1):
            return self.waypoints[index_way_point - (len(self.waypoints))]
        elif index_way_point < 0:
            return self.waypoints[len(self.waypoints) + index_way_point]
        else:
            return self.waypoints[index_way_point]

    @staticmethod
    def get_way_points_distance(previous_waypoint, next_waypoint):
        return math.sqrt(
            pow(next_waypoint[1] - previous_waypoint[1], 2) + pow(next_waypoint[0] - previous_waypoint[0], 2))

    @staticmethod
    def get_heading_between_waypoints(previous_waypoint, next_waypoint):
        track_direction = math.atan2(next_waypoint[1] - previous_waypoint[1], next_waypoint[0] - previous_waypoint[0])
        return math.degrees(track_direction)

    def get_car_heading_error(self):  # track direction vs heading
        next_point = self.get_way_point(self.closest_waypoints[1])
        prev_point = self.get_way_point(self.closest_waypoints[0])
        track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
        track_direction = math.degrees(track_direction)
        return track_direction - self.heading

    def get_optimum_speed_ratio(self):
        if abs(self.get_car_heading_error()) >= self.MAX_STEERING_ANGLE:
            return float(0.34)
        if abs(self.get_car_heading_error()) >= (self.MAX_STEERING_ANGLE * 0.75):
            return float(0.67)
        current_position_xy = (self.x, self.y)
        current_wp_index = self.closest_waypoints[1]
        length = self.get_way_points_distance((self.x, self.y), self.get_way_point(current_wp_index))
        current_track_heading = self.get_heading_between_waypoints(self.get_way_point(current_wp_index),
                                                                   self.get_way_point(current_wp_index + 1))
        while True:
            from_point = self.get_way_point(current_wp_index)
            to_point = self.get_way_point(current_wp_index + 1)
            length = length + self.get_way_points_distance(from_point, to_point)
            if length >= self.SAFE_HORIZON_DISTANCE:
                heading_to_horizont_point = self.get_heading_between_waypoints(
                    self.get_way_point(self.closest_waypoints[1]), to_point)
                if abs(current_track_heading - heading_to_horizont_point) > (self.MAX_STEERING_ANGLE * 0.5):
                    return float(0.33)
                elif abs(current_track_heading - heading_to_horizont_point) > (self.MAX_STEERING_ANGLE * 0.25):
                    return float(0.66)
                else:
                    return float(1.0)
            current_wp_index = current_wp_index + 1

    def get_turn_angle(self):
        current_waypoint = self.closest_waypoints[0]
        angle_ahead = self.get_heading_between_waypoints(self.get_way_point(current_waypoint),
                                                         self.get_way_point(current_waypoint + 1))
        angle_behind = self.get_heading_between_waypoints(self.get_way_point(current_waypoint - 1),
                                                          self.get_way_point(current_waypoint))
        result = angle_ahead - angle_behind
        if angle_ahead < -90 and angle_behind > 90:
            return 360 + result
        elif result > 180:
            return -180 + (result - 180)
        elif result < -180:
            return 180 - (result + 180)
        else:
            return result

    # Indicates the car is in turn
    def is_in_turn(self):
        return abs(self.get_turn_angle()) >= self.ANGLE_IS_CURVE

    # Indicates the car has reached final waypoint of the circuit track
    def reached_target(self):
        max_waypoint_index = len(self.waypoints) - 1
        return self.closest_waypoints[1] == max_waypoint_index

    def get_expected_turn_direction(self):
        current_waypoint_index = self.closest_waypoints[1]
        length = self.get_way_points_distance((self.x, self.y), self.get_way_point(current_waypoint_index))
        while True:
            from_point = self.get_way_point(current_waypoint_index)
            to_point = self.get_way_point(current_waypoint_index + 1)
            length = length + self.get_way_points_distance(from_point, to_point)
            if length >= self.SAFE_HORIZON_DISTANCE * 4.5:
                result = self.get_heading_between_waypoints(self.get_way_point(self.closest_waypoints[1]), to_point)
                if result > 2:
                    return "LEFT"
                elif result < -2:
                    return "RIGHT"
                else:
                    return "STRAIGHT"
            current_waypoint_index = current_waypoint_index + 1

    def is_in_optimized_corridor(self):
        if self.is_in_turn():
            turn_angle = self.get_turn_angle()
            if turn_angle > 0:  # Turning LEFT - better be by left side
                return (self.is_left_of_center == True and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD * 2 * self.track_width) or
                        self.is_left_of_center == False and self.distance_from_center <= (
                                self.CENTERLINE_FOLLOW_RATIO_TRESHOLD / 2 * self.track_width))
            else:  # Turning RIGHT - better be by right side
                return self.is_left_of_center == True and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD / 2 * self.track_width) or self.is_left_of_center == False and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD * 2 * self.track_width)
        else:
            next_turn = self.get_expected_turn_direction()
            if next_turn == "LEFT":  # Be more righ side before turn
                return self.is_left_of_center == True and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD / 2 * self.track_width) or self.is_left_of_center == False and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD * 2 * self.track_width)
            elif next_turn == "RIGHT":  # Be more left side before turn:
                return self.is_left_of_center == True and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD * 2 * self.track_width) or self.is_left_of_center == False and self.distance_from_center <= (
                        self.CENTERLINE_FOLLOW_RATIO_TRESHOLD / 2 * self.track_width)
            else:  # Be aligned with center line:
                return self.distance_from_center <= (self.CENTERLINE_FOLLOW_RATIO_TRESHOLD * 2 * self.track_width)

    def is_optimum_speed(self):
        return abs(self.speed - (self.get_optimum_speed_ratio() * self.MAX_SPEED)) < (
                self.MAX_SPEED * 0.15) and self.MIN_SPEED <= self.speed <= self.MAX_SPEED

    def evaluate(self):
        self.init_self(self.params)
        result_reward = float(0.001)
        try:
            # No reward => Fatal behaviour, NOREWARD!  (out of track, reversed, sleeping)
            if self.all_wheels_on_track == False or self.is_reversed == True or (self.speed < (0.1 * self.MAX_SPEED)):
                return float(self.PENALTY_MAX)

            # REWARD 50 - EARLY Basic learning => easy factors accelerate learning
            # Right heading, no crazy steering
            if abs(self.get_car_heading_error()) <= self.SMOOTH_STEERING_ANGLE_TRESHOLD:
                result_reward = result_reward + self.REWARD_MAX * 0.3

            if abs(self.steering_angle) <= self.SMOOTH_STEERING_ANGLE_TRESHOLD:
                result_reward = result_reward + self.REWARD_MAX * 0.15

            # REWARD100 - LATER ADVANCED complex learning
            # Ideal path, speed wherever possible, carefully in corners
            if self.is_in_optimized_corridor():
                result_reward = result_reward + float(self.REWARD_MAX * 0.45)

            if not (self.is_in_turn()) and (abs(self.speed - self.MAX_SPEED) < (0.1 * self.MAX_SPEED)) \
                    and abs(self.get_car_heading_error()) <= self.SMOOTH_STEERING_ANGLE_TRESHOLD:
                result_reward = result_reward + float(self.REWARD_MAX * 1)

            if self.is_in_turn() and self.is_optimum_speed():
                result_reward = result_reward + float(self.REWARD_MAX * 0.6)

            # REWAR - Progress bonus
            TOTAL_NUM_STEPS = 150
            if (self.steps % 100 == 0) and self.progress > (self.steps / TOTAL_NUM_STEPS):
                result_reward = result_reward + self.REWARD_MAX * 0.4

            # Reach Max Waypoint - get extra reward
            if self.reached_target():
                result_reward = float(self.REWARD_MAX)

        except Exception as e:
            print(e)

        # Finally - check reward value does not exceed maximum value
        if result_reward > self.REWARD_MAX:
            result_reward = self.REWARD_MAX

        return float(result_reward)


def reward_function(params):
    deep_racer = DeepRacer(params)
    return float(deep_racer.evaluate())
