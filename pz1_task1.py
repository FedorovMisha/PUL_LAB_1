import math


# 9 - Вариант
# Написать программу для расчета площади, периметра (длины окружности) по заданным параметрам (вводятся с клавиатуры):
# 9. Правильного пятиугольника (по длине стороны)

#   S = n/4 × a2 × ctg(pi/n), где n – количество сторон фигуры, a – длина стороны.

# Расчет площади правильного многоугольника по длине стороны и кол-ву сторон
def get_square_by_side(sideSize, sideCount):
    square = (sideCount / 4) * math.pow(sideSize, 2) * (math.cos(3.14 / sideCount) / math.sin(3.14 / sideCount))
    return square


# Рачет периметра многоугольника
def get_perimeter(sideSize, sideCount):
    return sideSize * sideCount


figureSideCount = 5
figureSideSize = float(input("Введите размер стороны многоугольника: "))

print("Периметр = ", get_perimeter(figureSideSize, figureSideCount))
print("Площадь = ", get_square_by_side(figureSideSize, figureSideCount))

