class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(output, index):
            if index == len(s):
                result.append("".join(output))
                return
            char = s[index]
            if char.isnumeric():
                output.append(char)
                backtrack(output, index + 1)
                output.pop()
            else:
                output.append(char.lower())
                backtrack(output, index + 1)
                output.pop()

                output.append(char.upper())
                backtrack(output, index + 1)
                output.pop()

        backtrack([], 0)
        
        return result