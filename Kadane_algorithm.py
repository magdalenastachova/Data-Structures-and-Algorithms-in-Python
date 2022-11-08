# find the largest contiguous subarray sum in a given array in O(n) time complexity and O(1) space complexity
from math import inf

def kadane(my_arr):
    result=-inf
    temp=0

    for item in my_arr:
        temp += item

        if result < temp: result=temp

        if temp < 0: temp=0

    return result

input=[-2,1,-3,4,-1,2,1,-5,4]
print(kadane(input))