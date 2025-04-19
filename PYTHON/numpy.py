import numpy as np

a = np.ones((5, 5))#for making all elements 1 of a 5*5 matrix
a[1, 1:4] = 0  #for making all elements 0 of row
a[3,1:4]=0
a[2, 2] = 9  
a[1:4,1]=0
a[1:4,3 ]=0
print(a)
