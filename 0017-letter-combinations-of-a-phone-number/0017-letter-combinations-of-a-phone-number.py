class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        res = [""]


        for digit in digits:
            newRes = []
            for combination in res:
                for letter in digitToChar[digit]:
                    newRes.append(combination + letter)
            res = newRes

        return res
