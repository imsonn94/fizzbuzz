#def fibo(num):
#    if num <= 2:
#        return 2
#    else:
#        return fibo(num-1)+fibo(num-2)
from math import sqrt
def fibo(num):
    phi = (1 + sqrt(5)) / 2
    return round(pow(phi, num) / sqrt(5))

print(fibo(5))
