#simple interest program
principle = int(input("enter how much money:"))
rate = float(input("enter rate of interest:"))
time = int(input("enter time of years:"))

simple_interest  = (principle * rate * time)/100
print("principle:{}\nrate:{}\ntime:{}\nsimple interest is:{}".format(principle,rate,time,simple_interest))