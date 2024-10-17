import math


beijing = (39.9075000, 116.3972300) 
kyiv = (50.4546600, 30.5238000)      

x1 = math.radians(beijing[0])
y1 = math.radians(beijing[1])
x2 = math.radians(kyiv[0])
y2 = math.radians(kyiv[1])


distance = 6371.032 * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

print("{:>10} km".format(round(distance, 3)))