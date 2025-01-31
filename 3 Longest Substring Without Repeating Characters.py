# Solution 1 
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        char_dict = defaultdict()
        max_length = 0
        index = 0
        while index < len(s):
            char = s[index]
            if char in char_dict:
                index = char_dict[char] + 1
                if len(char_dict) > max_length:
                    max_length = len(char_dict)
                char_dict = defaultdict()
            else:
                char_dict[char] = index
                index += 1
        return max(max_length, len(char_dict))
