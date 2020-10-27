def reward_function(params):
    """
    Reward function focused on making the agent to stay inside the two borders of the track while increasing speed
    """

    # Read input parameters
    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    speed = params['speed']

    # Give a very low reward by default
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the car is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 5.0

    if speed < 0.5:
        reward += 1
    elif speed < 1:
        reward += 2
    elif speed < 2:
        reward += 3
    elif speed < 3:
        reward += 4
    else:
        reward += 5

    # Always return a float value
    return reward
