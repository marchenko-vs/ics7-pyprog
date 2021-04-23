# Программа вычисляет объем правильной призмы, вписанной в цилиндр и
# площади ее боковой и полной поверхностей.
# Автор программы - Марченко Владислав. Группа ИУ7-13Б.

import math


cylinder_height = float(input('Введите высоту цилиндра: '))
cylinder_base_radius = float(input('Введите радиус основания цилиндра: '))

if cylinder_height <= 0 or cylinder_base_radius <= 0:
    print('Ошибка: введены некорректные данные')
else:
    prism_base_height = 1.5 * cylinder_base_radius
    prism_base_side = (2 * prism_base_height) / math.sqrt(3)
    prism_base_area = (prism_base_side ** 2 * math.sqrt(3)) / 4
    prism_volume = prism_base_area * cylinder_height
    lateral_surface_area = prism_base_side * cylinder_height * 3
    total_surface_area = lateral_surface_area + 2 * prism_base_area
    
    print('\nОбъем призмы равен {:7.4f}'.format(prism_volume))
    print('Площадь боковой поверхности призмы равна' 
            ' {:7.4f}'.format(lateral_surface_area))
    print('Площадь полной поверхности призмы равна' 
            ' {:7.4f}'.format(total_surface_area))

