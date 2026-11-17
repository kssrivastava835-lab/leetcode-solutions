class Solution(object):
    def generateParenthesis(self, n):
        result = []
        def backtrack(current,open_current,close_current):
            if len(current) == 2*n:
                result.append(current)
                return 
            
            if open_current < n:
                backtrack(current + "(" , open_current + 1, close_current)

            if close_current < open_current:
                backtrack(current + ")", open_current,close_current + 1)

        backtrack("",0,0)

        return result
            
