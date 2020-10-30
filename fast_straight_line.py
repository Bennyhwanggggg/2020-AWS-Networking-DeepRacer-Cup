def reward_function(params):
    """
    Reward function focused on making the agent to stay inside the two borders of the track and fast when straight line
    """

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    is_offtrack = params['is_offtrack']
    speed = params['speed']
    steering_angle = params['steering_angle']
    heading = params['heading']

    # Give a very low reward by default
    reward = 1e-3

    if is_offtrack:
        return -10.0
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward += 5.0
    if (-5 < heading < 5) or heading < -175 or heading > 175:
        if speed < 1.5:
            reward -= 3
        elif speed < 2.8:
            reward += 1
        else:
            reward += 10

    if -5 < steering_angle < 5 and (-5 < heading < 5) or heading < -175 or heading > 175:
        reward += 10

    return reward
