import random
#пункт_1
m = int(input(("Вкажіть модуль для подальших розрахунків: m = ")))
#пункт_2
a = int(input(("Вкажіть число для розрахунку такого рівняння:x=a mod m. a = ")))
x = a%m
print("a mod m = ", x)
#пункт_3
b = int(input(("Вкажіть число степення для розрахунку такого рівняння:x=(a^b) mod m. b = ")))
y = (a**b)%m
print("(a^b) mod m = ", y)

#пункт_5
n = int(input("Вивід простих чисел від 0 до "))
a = [0] * n
for i in range(n):
    a[i] = i

a[1] = 0

f = 2
while f < n:
    if a[f] != 0:
        j = f * 2
        while j < n:
            a[j] = 0
            j = j + f
    f += 1


b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])

        
del a
print (b)
