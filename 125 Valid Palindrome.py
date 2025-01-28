class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = ""
        for char in s:
            if char.isalnum():
                phrase += char.lower()
        start = 0
        end = len(phrase) - 1
        while start <= end:
            if phrase[start] != phrase[end]:
                return False
            start += 1
            end -= 1
        return True
