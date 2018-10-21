import numpy as np
from scipy.interpolate import RectBivariateSpline
z = np.ones((5,10))
z[3,3:5] = [1,2]

p = np.ones((2,1))
z=np.concatenate((p,p),axis=1)
print(z)

# x=np.arange(5)
# y=np.arange(7)
#
# func = RectBivariateSpline(x,y,z)
#
# x1 = np.linspace(1,4,3)
# y1 = np.linspace(2,5,5)
#
# print(x1)
# z1=func.__call__(x1,y1)
# # z2=func.ev(x1,y1,0,1)
# print(z1,'-------')