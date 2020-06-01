import random
from MapCreator.MapFuncs import generate_map

#Random' coordinates near the central point.
def random_acot_point(point, n):
	points = [(point[0]+random.choices([-1, 1])[0]*random.randrange(1, 2*n)/10, 
			   point[1]+random.choices([-1, 1])[0]*random.randrange(1, 2*n)/10) 
			   for _ in range(n)]
	points = tuple(set(points+[point]))
	return points
	
#Sequential and random node connection.
def aleatore_nodes(points, n):
	nodes = [*zip(points, (points[-1],)+points[:-1])]

	for _ in range(n):
		nodes.append((*random.choices(points), *random.choices(points)))
		
	return tuple(nodes)
	
	
if __name__ == '__main__':
	#Central test point.
	punto = (41.257160, -95.995102)
	
	points = random_acot_point(punto, 15)
	nodes = aleatore_nodes(points, 1)
	
	#test
	generate_map(punto, points, nodes, 'Test')
	