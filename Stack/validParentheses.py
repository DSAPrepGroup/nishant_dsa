class Solution1:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]"in s or "{}" in s:
            s = s.replace("()","")
            s = s.replace("[]","")
            s = s.replace("{}","")
        return s == ""
        


class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []
        hashMap = {")":"(", "]":"[","}":"{"}

        for i in s:
            if i in hashMap:
                if stack  and stack[-1]==hashMap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
