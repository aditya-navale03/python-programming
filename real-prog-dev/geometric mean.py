#geometric mean
import numpy as np
def g_mean(x):
    a = np.log(x)
    return np.exp(a.mean())

g_mean([1,2,3,54,5,43,3,4,55,])