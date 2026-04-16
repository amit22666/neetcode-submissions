class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

#Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
        stack = []
        result = []
        def backtrack(CountOpen, CountClose):
            
            if CountOpen == CountClose == n:
                result.append("".join(stack))
                return
            
            if CountOpen<n:
                stack.append("(")
                backtrack(CountOpen+1,CountClose)
                stack.pop()

            if CountClose<CountOpen:
                stack.append(")")
                backtrack(CountOpen,CountClose+1)
                stack.pop()

        backtrack(0,0)
        return result
        # create stack
        # create result

        # backtrack(openIndex, closeIndex)
        # if openIndex == closeIndex == n
            # we found the result
            # res append ("".join(stack))
        # open case 
        #if openN < n
            # stack append open bracket
            # backtrack(next open index, closed index)
            # stack pop
        
        # close case FOR BALANCE CLOSE SHOULD BE LESS THAN OPEN
        # if closedN < openN 
        # stack append close bracket
        # backtrack(open index, next closed index)
        # stack pop

    # backtrack(0,0)
    # return res
