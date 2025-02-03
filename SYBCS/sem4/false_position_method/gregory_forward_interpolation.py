#forward difference table 

#create table
import numpy as np
n = int (input("enter number of data points"))
x = np.zeros((n))
y = np.zeros((n, n))

print("enter data for x and y:")

for i in range(n):
    x[i] = float(input("x[" + str(i) + "]="))
    y[i][0] = float(input("y ["+str(i)+ "]="))
    

for i in range(1, n):
    for j in range(0, n-i):
        y[j][i] = y[j+i][i-1]-y[j][i-1]
print("\nforward difference table\n")

for i in range(0, n):
    print("%0.2f" % (x[i]),end =" ")
    for  j in range(0,n-1):
        print("| | %0.2f" % (y[i][j]),end = " ")
    print()
    
#calculation u mentioned in the formula
def u_cal(u, n):
    temp = u
    for i in range(1, n):
        temp = temp * (u-i)
    return temp

#calculating factorial of given 
def fact(n):
    f = 1
    for i in range(2, n+1):
        f *= i
    return f

#calculating at interpolated value by using forward difference formula
value = float(input("value:"))
sum = y[0][0]
u = (value - x[0]) / (x[1] - x[0])
for i in range(1, n):
    sum = sum + (u_cal(u, i) * y[0][i]) / fact(i)
print("\n Value at",value,"is", round(sum, 6))
