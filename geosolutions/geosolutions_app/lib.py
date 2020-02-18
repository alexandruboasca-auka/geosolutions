import math

def find_points(points_arr, search_point, no_points, operation):
	# If searching for a greater number of points than available, we can only return all the points
	if no_points > len(points_arr):
		no_points = len(points_arr)

	points_distance = []

	for p in points_arr:
		points_distance.append({
			'point': p,
			'distance': math.sqrt(((p[0] - search_point[0]) ** 2) + ((p[1] - search_point[1]) ** 2))
		})

	points_distance.sort(key=lambda x: x['distance'])

	if operation == 'N':
		return points_distance[: no_points]

	if operation == 'F':
		return sorted(points_distance[len(points_arr) - no_points: ], key=lambda x: x['distance'], reverse=True)
