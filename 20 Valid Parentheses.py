# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char not in mapping:
                stack.append(char)
            else:
                if len(stack) != 0 and stack[-1] == mapping[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
