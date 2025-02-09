'''
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that satisfy the condition.
Return the answer with the smaller index first.

Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
'''

# approach 1 (brute force)
class solution1:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
    n = len(nums)
    for i in range(n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

# approach 2 hashMap value:index
class solution1:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
    hashMap={}
    for i , n in enumerate(nums):
        diff = target - n
        if diff in hashMap:
            return[hashMap[diff], i]
        hashMap[n] = i
    return
