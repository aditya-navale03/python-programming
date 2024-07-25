#Q.generate all relative prime numbers to 111 < 150
import math as m
def phi(n):
    for i in range(1,n):
        if m.gcd(n, i)==1:
            print(i,end=" ")
phi(111)
