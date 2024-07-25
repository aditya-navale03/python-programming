#Q..write python code to find value of function f(x,y) = x sqr - 2xy +4   at the point (2,0,1,-1)
def val_functn(x,y):
    return x ** 2 - 2 * x*y + 4
x1 = 2
x2 = -1
result = val_functn(x1,x2)
print(f"value of funtion at f(x,y):{x1,x2} is :{result}")
