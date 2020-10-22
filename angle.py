import math

def getAngle(a, b, c):
    ang = math.degrees(math.atan2(c[1]-b[1], c[0]-b[0]) - math.atan2(a[1]-b[1], a[0]-b[0]))
    return ang + 360 if ang < 0 else ang

print(getAngle((44.587662,-123.256691), (44.58762,-123.256981), ( 44.587589,-123.257622)))
