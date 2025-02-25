class Solution1:
    def hasDuplicate(self, nums: List[int]) -> bool:
        m = {}
        for i in range(len(nums)):
            if(nums[i] in m):
                return True
            m[nums[i]] = True
        return False

class Solution2:
    def hasDuplicate(self, nums: List[int]) -> bool:
      set_nums = set(nums)
         if len(nums) == len(set_nums):
            return False
         else :
            return True