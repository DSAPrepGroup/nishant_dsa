"""
size of the window - most occuring character < k
"""

class Solution1:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            while(r-l+1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)
        return res


class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for i in range(len(s)):
            count = {}
            maxf = 0
            for j in range(i, len(s)):
                count[s[j]] = 1 + count.get(s[j],0)
                maxf =  max(maxf, count[s[j]])
                if (j-i +1) - maxf <= k:
                    res = max(res, j-i+1)
        return res


