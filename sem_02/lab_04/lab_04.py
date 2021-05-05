import math

coords = [[0, 0],
          [0, 20],
          [20, 0]]
result_matrix = [[0, 0],
                 [-4, -2],
                 [3, 7]]

ab_x = coords[1][0] - coords[0][0]
ab_y = coords[1][1] - coords[0][1]
ab = math.sqrt(ab_x * ab_x + ab_y * ab_y)

bc_x = coords[2][0] - coords[1][0]
bc_y = coords[2][1] - coords[1][1]
bc = math.sqrt(bc_x * bc_x + bc_y * bc_y)

ac_x = coords[2][0] - coords[0][0]
ac_y = coords[2][1] - coords[0][1]
ac = math.sqrt(ac_x * ac_x + ac_y * ac_y)

half_p = (ab + bc + ac) / 2
triangle_s = math.sqrt(half_p * (half_p - ab) * (half_p - bc) * (half_p - ac))

circle_r = (ab * bc * ac) / (4 * triangle_s)
circle_s = circle_r ** 2 * math.pi

result = circle_s - triangle_s

num_of_dots = len(coords)
for i in range(num_of_dots):
    first_x = coords[i][0]
    first_y = coords[i][1]
    for j in range(num_of_dots):
        second_x = coords[j][0]
        second_y = coords[j][1]
        if second_x != first_x and second_y != first_y:
            for k in range(num_of_dots):
                third_x = coords[k][0]
                third_y = coords[k][1]
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
                        result_matrix[0] = [coords[i][0],
                                            coords[i][1]]
                        result_matrix[1] = [coords[j][0],
                                            coords[j][1]]
                        result_matrix[2] = [coords[k][0],
                                            coords[k][1]]

for i in range(len(result_matrix)):
    for j in range(len(result_matrix[i])):
        print(result_matrix[i][j], end=' ')
    print()

print(result)