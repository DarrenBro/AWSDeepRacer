import math
def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    
    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    
    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 2.0
    elif distance_from_center <= marker_2:
        reward = 1.0
    elif distance_from_center <= marker_3:
        reward = 0.5
    else:
        reward = 1e-3  # likely crashed/ close to off track
    
    if params['progress'] >= 100:
        reward += 100
    elif params['progress'] >= 75:
        reward += 10
    elif params['progress'] >= 50:
        reward += 1
    elif params['progress'] >= 25:
        reward += .1
    
    prev_index = params['closest_waypoints'][0]
    next_index = params['closest_waypoints'][1]
    
    prev_way = params['waypoints'][prev_index]
    next_way = params['waypoints'][next_index]
    
    #slope = (next_way[1] - prev_way[1])/(next_way[0] - prev_way[0])
    rise = next_way[1] - prev_way[1]
    run = next_way[0] - prev_way[0]
    
    angle = math.atan(rise/run) * (180/math.pi)
    
    angle_dif = math.fabs(params['heading'] - angle)
    
    if angle_dif > 30.0:
        reward *= 0.9
        
    if angle_dif < 20.0:
        reward *= 1.1
        
    SPEED_THRESHOLD_1 = 2
    if params['speed'] < SPEED_THRESHOLD_1:
        reward *= 0.70
    
    SPEED_THRESHOLD_2 = 4
    if params['speed'] < SPEED_THRESHOLD_2:
        reward *= 0.9
    
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15
    
    # Penalize reward if the agent is steering too much
    if params['steering_angle'] > ABS_STEERING_THRESHOLD:
        reward *= 0.75
    
    if not params['all_wheels_on_track']:
        reward = 1e-3
    
    return float(reward)
