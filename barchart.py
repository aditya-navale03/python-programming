import matplotlib.pyplot as plt
import numpy as np

size = int(input("Enter how many bars to print for the barchart: "))

values = []
names = []

for _ in range(size):
    value = int(input("Enter value for the bar: "))
    name = input("Enter name for the bar: ")    
    values.append(value)
    names.append(name)
    
y = np.array(values)
x = np.array(names)

plt.bar(x, y)
plt.xlabel('Names')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()
