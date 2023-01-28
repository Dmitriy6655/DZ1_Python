# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

print('Введите трехзначное число: ')
a = input()
# a = int(239)
# flag = True
sum = int()
num = int()
#
# while a>0:
#     num=a%10
#     sum = a
#     a = a/10
#     sum = sum + a
# print(sum)

if len(a) > 3 or len(a) < 3:
    print("Введено не корректное число!")
    exit(0)
else:
    a = int(a)

while a>0:
    num=a%10
    a = a//10
    sum = sum + num
print(f'Сумма цифр числа равна: {sum}')
