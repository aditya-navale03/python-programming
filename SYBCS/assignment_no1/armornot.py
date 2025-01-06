import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2*np.pi, 2*np.pi, 1000)
f_x = np.sin(x)
g_x = np.cos(x)

plt.plot(x, f_x, label='f(x) = sin(x)', color='blue')
plt.plot(x, g_x, label='g(x) = cos(x)', color='red')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of f(x) = sin(x) and g(x) = cos(x)')



plt.show()
