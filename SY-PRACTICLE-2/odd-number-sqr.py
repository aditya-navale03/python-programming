#Q.square of odd numbers from 1 to 20 using while loop
n1 = 1
while(n1 < 21):
    if(n1 % 2 != 0):
        print(f"square of number{n1} is:{n1 ** 2}")
    n1 = n1 + 1
