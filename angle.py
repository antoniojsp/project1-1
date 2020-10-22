import math
#function that calculate the angle of three points.
def get_angle(before, center, after):
    ang = math.degrees(math.atan2(after[1]-center[1], after[0]-after[0]) - math.atan2(before[1]-center[1], before[0]-center[0]))
    result = ang + 360 if ang < 0 else ang
    return result
