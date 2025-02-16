
"""
nums = [-1,0,2,4,6,8]
target = 4
"""


class Solution1:
    def search(self, nums: List[int], target: int) -> int:
        output = 0
        for i in range(0, len(nums)):
            if nums[i] == target:
                output = i
                break
            else:
                output = -1
        
        return output



class Solution2:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l<=r:
            m = (l+r)//2
            if nums[m] > target:
                r = m-1
            elif nums[m] < target:
                l = m+1
            else:
                return m

        return -1