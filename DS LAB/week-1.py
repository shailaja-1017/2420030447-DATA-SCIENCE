

!pip install numpy

import numpy as np
a1 = np.array([1,2,3])
print(a1)

a2 = np.array([[4,5,6],[2,4,1]])
print(a1.ndim)

import numpy as np
p = np.zeros([1])
n = np.zeros([3,4])
print(p)
print(n)
print(type(n))

import numpy as np
p = np.ones([1])
n = np.ones([3,4])
print(p)
print(n)
print(type(n))

a3 = np.array([1,3,5,4,9,12,2,6])
print(a3[4])
print(a3[2:4])
print(a3[:7])
print(a3[5:])

import numpy as np

a4 = np.array([2,4,1,5,8,7])
print(a4)
print(a4.ndim)
print(a4.shape)
x = a4.reshape(2,3)
print(x)

import numpy as np
a1 = np.array([1,2,3])
a2 = np.array([4,5,6])
c = np.concatenate((a1,a2))
print(c)
s = np.split(c,3)
print(s)

import numpy as np
n1 = np.array([1,2,3,4])
n2 = np.array([4,5,6,7])
n3 = np.concatenate((n1,n2))
sp = np.array_split(n3,4)
print(sp[3])

import numpy as np
n1 = np.array([2,4,3,6,8])
p = np.where(n1==6)
print(p)

import numpy as np
n = np.array([4,7,2,6,5])
p = np.sort(n)
print(p)

m = np.array(['banana','apple','orange','cherry'])
f = np.sort(m)
print(f)

n1 = np.array([1,2,3,4])
n2 = np.array([3,5,2,6])
print(np.sum([n1,n2]))

n1 = np.array([1,2,3,4])
n2 = np.array([3,5,2,6])
print(np.sum([n1,n2],axis=1))

n1 = np.array([1,2,3,4])
n2 = np.array([3,5,2,6])
print(np.sum([n1,n2],axis=0))

n1 = np.array([1,2,3,4])
n2 = np.array([3,5,2,6])
print(np.sum((n1,n2)))

n1 = np.array([1,2,3,4])
n2 = np.array([3,5,2,6])
print(np.subtract([n1,n2]))
