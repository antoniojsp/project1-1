from distance import distance
from directions import get_name
#two points,
#janeth smith house
inicio_lat =  44.046074#degrees in decimals
inicio_lon = -122.932640
#7-11
final_lat =  44.040276
final_lon = -123.080187

print ("{:.2f} meters".format(distance(inicio_lat, inicio_lon, final_lat, final_lon)))
