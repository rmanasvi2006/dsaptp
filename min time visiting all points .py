def minTimeToVisitAllPoints(points):
    return sum(max(abs(points[i][0] - points[i-1][0]), abs(points[i][1] - points[i-1][1])) for i in range(1, len(points)))

points = [[1,1], [3,4], [-1,0]]
print(minTimeToVisitAllPoints(points))
