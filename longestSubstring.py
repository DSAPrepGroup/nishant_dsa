"""
we take a map and store the character as key and its index as value.
then we take 2 pointer left and right.
if the character is already present in map we move left pointer to its last occurence+1
we do this becoz the new sequence will start from +1 position.
if character is not in map we keep on moving the right pointer then store the char and index in map
and calculate the max by taking diff between right and left
return ans
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = {}
        left, right = 0,0
        ans = 0
        for i in range(len(s)):
            if s[i] in m:
                left = max(left, m[s[i]]+1)
            right += 1
            m[s[i]] = i
            ans = max(right-left, ans)
        return ans