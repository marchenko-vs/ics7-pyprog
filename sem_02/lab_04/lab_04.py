import math

coordinates = [[0, 0],
               [-4, -2],
               [3, 7],
               [3, 3],
               [-3, 8],
               [5, -1]]
result_matrix = [[0, 0],
                 [-4, -2],
                 [3, 7]]

ab_x = coordinates[1][0] - coordinates[0][0]
ab_y = coordinates[1][1] - coordinates[0][1]
ab = math.sqrt(ab_x * ab_x + ab_y * ab_y)

bc_x = coordinates[2][0] - coordinates[1][0]
bc_y = coordinates[2][1] - coordinates[1][1]
bc = math.sqrt(bc_x * bc_x + bc_y * bc_y)

ac_x = coordinates[2][0] - coordinates[0][0]
ac_y = coordinates[2][1] - coordinates[0][1]
ac = math.sqrt(ac_x * ac_x + ac_y * ac_y)

half_p = (ab + bc + ac) / 2
triangle_s = math.sqrt(half_p * (half_p - ab) * (half_p - bc) * (half_p - ac))

circle_r = (ab * bc * ac) / (4 * triangle_s)
circle_s = circle_r ** 2 * math.pi

result = circle_s - triangle_s

num_of_dots = len(coordinates)
for i in range(num_of_dots):
    first_x = coordinates[i][0]
    first_y = coordinates[i][1]
    for j in range(num_of_dots):
        second_x = coordinates[j][0]
        second_y = coordinates[j][1]
        if second_x != first_x and second_y != first_y:
            for k in range(num_of_dots):
                third_x = coordinates[k][0]
                third_y = coordinates[k][1]
                if (third_x != second_x and third_y != second_y) and \
                        (third_x != first_x and third_y != first_y):
                    ab_x = second_x - first_x
                    ab_y = second_y - first_y
                    ab = math.sqrt(ab_x * ab_x + ab_y * ab_y)

                    bc_x = third_x - second_x
                    bc_y = third_y - second_y
                    bc = math.sqrt(bc_x * bc_x + bc_y * bc_y)

                    ac_x = third_x - first_x
                    ac_y = third_y - first_y
                    ac = math.sqrt(ac_x * ac_x + ac_y * ac_y)

                    half_p = (ab + bc + ac) / 2
                    triangle_s = math.sqrt(half_p * (half_p - ab) *
                                           (half_p - bc) * (half_p - ac))

                    circle_r = (ab * bc * ac) / (4 * triangle_s)
                    circle_s = circle_r ** 2 * math.pi

                    difference = circle_s - triangle_s

                    if difference < result:
                        result = difference
                        result_matrix[0] = [coordinates[i][0],
                                            coordinates[i][1]]
                        result_matrix[1] = [coordinates[j][0],
                                            coordinates[j][1]]
                        result_matrix[2] = [coordinates[k][0],
                                            coordinates[k][1]]

for i in range(len(result_matrix)):
    for j in range(len(result_matrix[i])):
        print(result_matrix[i][j], end=' ')
    print()

print(result)