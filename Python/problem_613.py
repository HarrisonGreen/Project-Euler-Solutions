from scipy import integrate
import numpy as np

f = lambda y, x: np.arctan2(3-y, -x) - np.arctan2(-y, 4-x)
a = integrate.dblquad(f, 0, 4, lambda x: 0, lambda x: 3 - 3*x/4)
print(round(a[0]/(12*np.pi), 10))
