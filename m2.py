# Факториалом натурального числа n называется произведение всех натуральных чисел от 1 до n. 
# Например, 4! =1 · 2 · 3 · 4 =24. На вход программы поступает положительное число A. 
# Необходимо вывести минимальное натуральное K, для которого 1! + 2! + ... + K! > A. 

A = int(input())
k = 1
f = 1
while s < A:
    s=1
    f *= k
    k += 1
    s += f
print(k)
