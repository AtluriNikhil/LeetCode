# Solution 1
# https://www.youtube.com/watch?v=tkNWKvxI3mU&ab_channel=GregHogg
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        right = 0
        count = [0] * 26

        while right < len(s):
            count[ord(s[right]) - 65] += 1
            window_size = right - left + 1
            max_frequency = max(count)
            
            while window_size - max_frequency > k:
                count[ord(s[left]) - 65] -= 1
                left += 1
                window_size = right - left + 1
            right += 1
            if longest < window_size:
                longest = window_size
        return longest
