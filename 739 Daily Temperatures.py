# Solution 1
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for index in range(len(temperatures)-1, -1, -1):
            temperature = temperatures[index]
            while stack:
                if stack[-1][0] > temperature:
                    break
                else:
                    stack.pop()
            if stack:
                result[index] = stack[-1][1] - index
            stack.append([temperature, index])
        return result
