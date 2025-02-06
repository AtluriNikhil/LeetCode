class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(openBrackets, closeBrackets, s):
            if openBrackets == closeBrackets and openBrackets + closeBrackets == n*2:
                result.append(s)
                return
            
            if openBrackets < n:
                backtrack(openBrackets + 1, closeBrackets, s + "(")
            
            if closeBrackets < openBrackets:
                backtrack(openBrackets, closeBrackets + 1, s + ")")
        
        backtrack(0, 0, "")

        return result
