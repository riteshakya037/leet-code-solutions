class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = []
        for i in s:
            if i == ")":
                x = stack.pop()
                while x != "(":
                    ans.append(x)
                    x = stack.pop()
                for j in ans:
                    stack.append(j)
                ans = []
            else:
                stack.append(i)
        return "".join(stack)
