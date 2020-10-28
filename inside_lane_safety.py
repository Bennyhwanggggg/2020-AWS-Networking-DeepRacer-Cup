def reward_function(params):
    """
    Reward function focused on making the agent to stay inside the two borders of the track and slow down when near
    way points for safety
    """

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_crashed = params['is_crashed']
    is_offtrack = params['is_offtrack']
    speed = params['speed']
    closest_waypoints_x, closest_waypoints_y = params['closest_waypoints']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the car is somewhere in between the track borders
    if not (is_crashed or is_offtrack) and (all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05):
        reward += 5.0

    if speed > 3 and closest_waypoints_x*closest_waypoints_x + closest_waypoints_y*closest_waypoints_y < 0.5*0.5:
        reward /= 2
    elif speed < 1:
        reward /= 3
    elif speed > 2:
        reward += 3

    # Always return a float value
    return reward
