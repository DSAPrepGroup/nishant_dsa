"""
example heights = [5,9,2,1,4]
area = length * width
length = min(5,4) as water cannot overflow
width will be diff of indexes

"""



class Solution1:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        for i in range (0,n):
            for j in range (i+1,n):
                length = min(heights[i],heights[j])
                width = j-i
                area = length * width
                max_area = max(max_area,area)
        return max_area


# two pointers

"""
we move the left pointer if its less than right pointer
and move the right pointer if its less than left pointer
becoz we want to calculate the max water area
"""
class Solution2:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        n = len(heights)
        l = 0
        r = n-1
        while(l<r):
            length = min(heights[l], heights[r])
            width = r-l
            area = length * width
            max_area = max(max_area, area)
            if heights[l] < heights[r]:
                l = l+1
            else:
                r=r-1
        return max_area