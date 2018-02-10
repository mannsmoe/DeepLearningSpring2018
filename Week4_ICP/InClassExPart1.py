import numpy as np
x = np.array([2, 3, 1, 0])
print(x)
y=np.random.randint(100, size=100)
y=y.reshape(10,10)
print('The 10x10 randomly generated array is : \n')
print(y)
print(2*'\n')
for i in range(10):
    z=y[i,:]
    print('Raw # ' + str(i+1) + ' is : ' + str(z))
    zm=max(z)
    print('Max of Raw # ' + str(i+1) + ' is : ' + str(zm))
    zn = min(z)
    print('Min of Raw # ' + str(i+1) + ' is : ' + str(zn))