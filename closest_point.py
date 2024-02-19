import math
def euclidean_distance(point):
    return math.sqrt(point[0]**2 + point[1]**2)

def closest_points(points,k):
    for i in range(k):
        closest_point=i
        for j in range(i+1,len(points)):
            if  euclidean_distance(points[j])<euclidean_distance(points[closest_point]):
                closest_point=j
        points[i],points[closest_point]=points[closest_point],points[i]

    return points[:k]

# Test case
points = [(3, 2), (1, 1), (2, 3)]
k = 2  # Number of closest points to find
closest_points_calculate = closest_points(points, k)
print("Closest points:", closest_points_calculate)


