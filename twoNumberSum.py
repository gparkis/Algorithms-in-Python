"""
Write a function that takes in a non-empty array of distinct integers and an integer representing a target sum. If any two numbers in the input array sum up to the target sum, the function should return them in an array, in sorted order. If no two numbers sum up to the target sum, the function should return an empty array. Assume that there will be at most one pair of numbers summing up to the target sum.

Sample input: [3, 5, -4, 8, 11, 1, -1, 6], 10
Sample output: [-1, 11]

"""

def twoNumbersSum(array, targetsum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetsum:
            return [array[left], array[right]]
        elif currentSum < targetsum:
            left += 1
        elif currentSum > targetsum:
            right -=1
    return []


output = twoNumbersSum([3, 5, -4, 8, 11, 1, -1, 6], 10)
print(output)

"""
time: O(nlog(n))
space: o(1)

if done with hash, space = o(n)

left and right pointer
sum the pointers
the if condition is determining if the left or right pointer will shift by comparing the sum to the target
moving right pointer will give smaller sum
moving left pointer will give larger sum 
"""