import numpy as np
import matplotlib.pyplot as plt

N=100
x=np.random.rand(N)
y=np.random.rand(N)
z=np.random.rand(N)

var_x=[i for i,j in zip(x,y) if i**2+j**2<1]
var_y=[j for i,j in zip(x,y) if i**2+j**2<1]


print('%s 개의 점 중 %s개'%(N,len(var_x)))
print('%s / %s * 4 = %s'%(len(var_x), N ,len(var_x) / N * 4))

c=plt.Circle((0,0),1,fc='w',ec='b')
a=plt.axes(xlim=(-1,1),ylim=(-1,1))
a.add_patch(c)
a.set_aspect('equal')
plt.grid(True, axis='both',color='black', alpha=1, linestyle='-')
plt.rcParams["figure.figsize"] = (10,10)
plt.plot(var_x,var_y)

plt.show()    
