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