#CS 162 - python array assignment with numpy
#Emma Nessly

import numpy as np

#1: Building the array
array = np.random.randint(1,10, size=(5,5), dtype=int)

#2: printing the array
print(array)

#3: printing the value of the 2nd row and third colum
print(f"The value of the number in the second row and third colum is: {array[1,2]}")

#4: printing the sum of all values in the array

array_sum = np.sum(array)
print(f"The sum of all values in the array is: {array_sum}")

#5: printing the mean of each row

print(f"The mean of each row in the array is: {np.mean(array, axis = 1)}")

#6: printing the maximum value of each colum of the array

max_array = np.max(array, axis = 0)
print(f"The maximum value in each colum of the array is: {max_array}")
