print("Выбрать и ввести выбранное значение")
print("Ввести с клавиатуры (1)")
print('или')
print("Рандомные числа (2)")
N = int(input("Введите число элементов массива: "))
A = [0] * N
I = int(input("Ваш выбор: "))
def  inter (x) :
    for i in range(N):
        A[i] = float(input())
def random(x):
    import random 
    for i in range(N):
        A[i] = random.uniform (-99,99)
if  I == 1:
    print ("Введите элементы массива ")
    inter (A)
elif I == 2:
        random (A)
print (A)
I = sorted (A)
R = I[-1]
print (R)
for i in range (N):
    if  i > A.index(R):
        A[i] = 0
        i = i + 1
print (A)
   
