# 15-16 sec, 4 hours, speed 6, gears 2

def reward_function(params):

    all_wheels_on_track = params['all_wheels_on_track']
    distance_from_center = params['distance_from_center']
    speed = float(params["speed"])
    track_width = (params["track_width"])

    reward = 1e-3

    if all_wheels_on_track and (0.5*track_width - distance_from_center) >= 0.15:
        if speed > 5:
          reward = speed + 20
        else:
          reward = speed

    if not all_wheels_on_track:
        reward *= -1

    return float(reward)
