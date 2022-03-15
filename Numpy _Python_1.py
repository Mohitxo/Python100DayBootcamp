# importing numpy libary in python
import numpy as np
myarr=np.array([[3,6,32,7]],np.int64)
myarr

# finding of an element using indexing in Array
myarr[0,1]

# arrayname.shape is used to tell the type of array
myarr.shape

myarr[0,1]=45
print(myarr)
data_type=type(myarr)
print(data_type)

#Array creation: Conversion from other python structures
listarray=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(listarray)
# dtype tell the dimensions of an array
print(listarray.dtype)
print(listarray.shape)
print(listarray.size)

# np.zeroes is used for making an array of given order where all the element is zero
zeroes=np.zeros((2,5))
print(zeroes)
print(zeroes.shape)
print(zeroes.size)

# np.arange is used to print the array of given order in arranged fashion 
range=np.arange(10)
print(range)
print(zeroes.shape)
print(zeroes.size)
print(zeroes.dtype)

# starting point, ending point and number of element you want in the array
lspace=np.linspace(1,5,5)  
print(lspace)

# np.identity is used to print an array of given order but that matrix will be an identity matrix means aii elements is equal to 1
identity_matrix=np.identity(5)
print(identity_matrix)
print(identity_matrix.shape)

arr=np.arange(25)
print(arr)
# reshape is used for reshape an array 
arr.reshape(5,5)

x=[[1,2,3],[4,5,6],[7,1,0]]
ar=np.array(x)
print(ar)

print(ar.sum(axis=0))
print(ar.sum(axis=1))

# too traspose an array using numpy
print(ar)
print(ar.T)

print(ar)
print(ar.flat)
for item in ar.flat:
  print(item)
  
# too check the dimension of an array we use ndim method
print(ar)
print(ar.ndim)
# to check totzl byte consume we will use nbyte method
print(ar.nbytes)

array1=np.array([19,1,11,23,45,98])
# argument to check the maximum and minimum number element indexed
print(array1.argmax())
print(array1.argmin())
# argsort is a argument which tell us which is the sort form of an array indexed wise
print(array1.argsort())


# Arrugment Method with 2D Matrix 
array_1=np.array([[11,22,33],[44,55,66],[77,88,99]])
print(array_1)

print("sorting an array axis wise \n",ar.argsort(axis=0))
print("finding max element axis wise",ar.argmax(axis=0))
print("finding min element axis wise",ar.argmin(axis=0))


x=[[1,2,3],[4,5,6],[7,1,0]]
ar=np.array(x)
print(ar)
# The numpy. ravel() functions returns contiguous flattened array(1D array with all the input-array elements and with the same type as it). 
print(ar.ravel())
print(ar.reshape(9,1))

# Adding two array 
x=[[1,2,3],[4,5,6],[7,1,0]]
ar1=np.array(x)
print("Array 1 \n",ar1)
y=[[1,1,1],[2,2,2],[3,3,3]]
ar2=np.array(y)
print("Array 2 \n",ar2)
print("Adding two array we will get \n",ar1+ar2)
print("Multiplication of an array \n",ar1*ar2)
print("squarer oot of an array \n",np.sqrt(ar1))


x=[[1,2,3],[4,5,6],[7,1,0]]
ar1=np.array(x)
print("Array 1 \n",ar1)
print("too count number of zeroes \n",np.count_nonzero(ar1))
