from math import sqrt


# Семинарские задачи
# a = int(input())
# print(a**2)

# a = int(input())
# b = int(input())
# if a>b:
#     print(a)
# else:
#     print(b)

# a = int(input())
# if a%2 == 0:
#     print("четное")
# else:
#     print("нечетное")

# n = int(input())
# for i in range(1, n+1):
#     print(i)

# max = 0
# for i in range(5):
#     a = int(input())
#     if a > max:
#         max = a
# print(max)

# a = int(input())
# b = int(input())
# if a == b**2:
#     print("а - квадрат b")
# elif b == a**2:
#     print("b - квардрат a")
# else: print("не являются квадратами")

# a = float(input())
# if a%1 != 0:
#     print(int(a*10%10))
# else:
#     print("число целое")

# a = int(input())
# if a%5 == 0 and (a%10 ==0 or a%15 == 0) and a%30 != 0:
#     print("кратно")
# else:
#     print("не кратно")



#Домашнее задание

# Задание 6
# a = int(input())
# if a in range(1, 5):
#     print("нет")
# elif a in range(6, 7):
#     print("да")
# else:
#     print("нет такого дня недели")

# Задание 8
# x, y = int(input("ВВедите число X ")), int(input("Введите число Y "))
# if x == 0 or y ==0:
#     print("Точка лежит на оси")
# elif x > 0:
#     if y > 0:
#         print("1 четверть")
#     else:
#         print("4 четверть")
# else:
#     if y > 0:
#         print("2 четверть")
#     else:
#         print("3 четверть")

#Задание 9
# che = int(input())
# if che == 1:
#     print("x > 0, y > 0")
# elif che == 2:
#     print("x < 0, y > 0")
# elif che == 3:
#     print("x < 0, y < 0")
# elif che == 4:
#     print("x > 0, y < 0")
# else:
#     print("нет такой четверсти")

# Задание 10
x1, x2 = float(input("Введите координаты точки 1 через точку (пример А(1;3) = 1.3 ")), \
         float(input("Введите координаты точки 2 через точку (пример А(1;3) = 1.3 "))
y1, y2, x1, x2 = int(x1 * 10 % 10), int(x2 * 10 % 10), int(x1), int(x2)
print(sqrt((x2-x1)**2 + (y2-y1)**2))
