a = int(input("enter the number to find armstrong or not:"))
n = a
while(n>0):
    r = n %10        
    a = (r* r* r)+a
    n= n/10
if(n == a):
    print("number is armstrong")
else:
    print("number is not armstrong")