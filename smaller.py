# y = mx + b
# m is slope, b is y-intercept

def compute_error_for_line_given_points(b, m, coordinates):
    totalError = 0
    for i in range(0, len(coordinates)):
        x = coordinates[i][0]
        y = coordinates[i][1]
        totalError += (y - (m * x + b)) ** 2
    return totalError / float(len(coordinates))
# example
print compute_error_for_line_given_points(1, 2, [[3,3],[6,9],[3,3]])