# 18-23 sec, 150min, speed 5, gears 3

def reward_function(params):

    on_track = params["all_wheels_on_track"]
    progress = float(params["progress"])
    speed = float(params["speed"])
    
    if not on_track:
        return float(0.0001)

    if progress == 100.0:
        return float(1000.0)
    
    return float(speed)
