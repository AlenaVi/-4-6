x = int(input("Введите число 0 ... 255: "))
if x >= 256:
    print ("Ошибка")
v = int(input("Введите целевую систему счисления (2 или 8): "))
def print_bin (n):
    k = 128 
    while k > 0:
        d = n // k 
        print(d , end="") 
        n = n % k 
        k = k // 2
if v == 2:
     print_bin(x) 
def from10ss(b):
    d = 0
    ss = 8
    while ss > 0:
       d = b // ss
       print(d, end="")
       b = b % ss
       ss = ss // 8
if v == 8:
    from10ss(x) 

