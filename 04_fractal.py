# -*- coding: utf-8 -*-

import simple_draw as sd

root = sd.get_point(300, 0)


def draw_branches(point, angle, length):
    if length < 10:
        return
    root_vector_1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    root_vector_1.draw()
    next_vector_1 = root_vector_1.end_point
    next_length_1 = length * (sd.random_number(75, 85) / 100)
    next_angle_1 = angle - sd.random_number(10, 30)
    next_angle_1_1 = angle + sd.random_number(15, 45)
    draw_branches(point=next_vector_1, angle=next_angle_1, length=next_length_1)
    draw_branches(point=next_vector_1, angle=next_angle_1_1, length=next_length_1)
    # root_vector_2 = sd.get_vector(start_point=root, angle=angle, length=length, width=3)
    # root_vector_2.draw()


draw_branches(root, 90, 100)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

sd.pause()


