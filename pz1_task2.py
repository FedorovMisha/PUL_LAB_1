# Рассчитать объём и полную поверхность по заданным параметрам (вводятся с клавиатуры):
# 2.	Параллелепипеда (по трем сторонам)

# Получить обьём паралеппипеда по трем сторонам
def get_parallelepiped_volume(sideA, sideB, sideC):
    return sideA * sideB * sideC


# Получить площадь полной поверхности параллепипеда
def get_full_parallelepiped_surface(sideA, sideB, sideC):
    return 2 * (sideA * sideB + sideA * sideC + sideB * sideC)


parallelepipedSideA, parallelepipedSideB, parallelepipedSideC = float(input("Введите сторону A: ")), \
                                                                float(input("Введите сторону B: ")), \
                                                                float(input("Введите сторону C: "))

print(" Обьем параллепипеда = ",
      get_parallelepiped_volume(parallelepipedSideA, parallelepipedSideB, parallelepipedSideC))
print(" Площадь полной поверхности параллепипеда = ",
      get_full_parallelepiped_surface(parallelepipedSideA, parallelepipedSideB, parallelepipedSideC))
