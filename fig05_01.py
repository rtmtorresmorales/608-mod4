# fig05_01.py Ramon Torres SEPT 2022
# Primitive bar Chart Function
import math
import decimal
import statistics


# creating an empty list
numbers = []
  
# number of elements as input
n = int(input("Enter number of data sets on your bar chart: , then enter each one and hit enter after each number"))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    numbers.append(ele) # adding the element

print('\nCreating a bar chart from numbers:')
print(f'Index{"Value":>8} Bar')

for index, value in enumerate(numbers):
	print(f'{index:>5}{value:>8}  {"*" * value}')
      


