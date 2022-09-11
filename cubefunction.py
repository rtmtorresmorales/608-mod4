#cubefunction.py Ramon Torres SEPT 2022
import math
import decimal
import statistics


# creating an empty list
numbers = []
  
# number of elements as input
n = int(input("Enter number of data sets on your list: , then enter each one and hit enter after each number"))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    numbers.append(ele) # adding the element
      

cube = []
for i in numbers: 
        cube.append(i*i*i)
print("The cubes for each element are: ", cube)
