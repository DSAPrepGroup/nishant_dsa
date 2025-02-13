class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]

        nums1 = [4,1,2]
        nums2 = [1,3,4,2]
        """
        ans = []
        for i, n in enumerate(nums1):
            a = -1
            for j in range(nums2.index(n), len(nums2)):
                if nums2[j] > n :
                    a = nums2[j]
                    break
            ans.append(a)
        return ans

