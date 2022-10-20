print("Выбрать и ввести выбранное значение для массива A") #Действия для массива A
print("Ввести с клавиатуры (1)")
print('или')
print("Рандомные числа (2)")
N = int(input("Введите число элементов массива: "))
A = [0] * N
I = int(input("Ваш выбор: "))
if  I == 1:
    print ("Введите элементы массива ")
    for i in range(N):
        A[i] = float(input())
elif I == 2:
    import random 
    for i in range(N):
        A[i] = random.uniform (-99, 99)
print (A)
print("Выбрать и ввести выбранное значение для массива B") #Действия для массива B
print("Ввести с клавиатуры (1)")
print('или')
print("Рандомные числа (2)")
N = int(input("Введите число элементов массива: "))
B = [0] * N
I = int(input("Ваш выбор: "))
if  I == 1:
    print ("Введите элементы массива ")
    for j in range(N):
        B[j] = float(input())
elif I == 2:
    import random 
    for j in range(N):
        B[j] = random.uniform (-99, 99)
print (B)
C =[]
for i in A:
    for j in B:
        if i == j:
            C.append(i)
            break
print(C)
