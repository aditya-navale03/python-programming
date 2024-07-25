#Q.find product of n natural number using while loop
n = int(input("enter any number:"))
prod = 1
i = 1
if(n > 0):
    while(i <= n):
       prod = prod * i
       i = i + 1
print(prod)
