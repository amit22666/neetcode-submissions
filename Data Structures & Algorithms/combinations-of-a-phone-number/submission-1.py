class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # digit[i], curAnswer
        # easy question
        res = []
        digitToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"qprs",
            "8":"tuv",
            "9":"wxyz",  
        }
    
        def backtrack(i, curAnswer):
            if len(digits) == len(curAnswer):
                res.append(curAnswer)
                return
            for c in digitToChar[digits[i]]:
                new_ans = curAnswer+c
                backtrack(i+1,new_ans )
        if digits:
            backtrack(0,"")
        return res