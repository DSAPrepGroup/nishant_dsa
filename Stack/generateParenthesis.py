"""
2 rules for backtracking:
- number of open and closed brackets will be equal to n
- closed will be less than open in positive case.

we follow these below things in code,
- only add open parenthesis if open < n and keep on backtracking until point 3
- only add closed if closed < open and keep on backtracking until point 3
- valid if open == closed == n
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
            
        backtrack(0,0)
        return res