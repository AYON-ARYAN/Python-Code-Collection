import numpy as np
d1=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
#create a 1d array
d2=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
array_2d=np.array(d2)#------------------syntax-------name.array(number of dimentions)
d3=[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]
array_3d=np.array(d3)#
print(array_2d)
print(array_3d)
print(np.zeros((2,3)))#------------something=name_of_array((dimention)) for zero array
print(np.ones((2,3)))#------------something=name_of_array((dimention)) for one array
print(np.eye(3))#-----------this is an identity matrix of 3 rows
print(np.arange(0,10,2))#------------this is an identity matrix of 3 row