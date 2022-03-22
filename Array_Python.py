from array import *
vals=array('i',[1,2,3,4,5,6,7,8,9,10])
print(vals) 

# Output:
# array('i', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# buffer info function tells the size of the array and memory location
print(vals.buffer_info())  

# output:
# (140366239608576, 10)

# too reverse an array we will use reverse function
arr=array('i',[2,4,6,8,10])
arr.reverse()
print(arr)

# output:
# array('i', [10, 8, 6, 4, 2])

# printing by indexing 
print(arr[1])
print(arr[2])
print(arr[3])

# output:
# 8
# 6
# 4

# too print element one by one element in an array we will use for loop
for i in range(5):
  print(arr[i])
  
# output:
# 10
# 8
# 6
# 4
# 2

