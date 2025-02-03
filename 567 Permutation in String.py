class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_freq = {}
        s2_freq = {}
        if s2_len < s1_len:
            return False
        for index in range(s1_len):
            s1_freq[s1[index]] = s1_freq.get(s1[index], 0) + 1
            s2_freq[s2[index]] = s2_freq.get(s2[index], 0) + 1

        for index in range(s2_len - s1_len):
            if s1_freq == s2_freq:
                return True           
            else:
                s2_freq[s2[index]] -= 1
                if s2_freq[s2[index]] == 0:
                    s2_freq.pop(s2[index])
                s2_freq[s2[index + s1_len]] = s2_freq.get(s2[index + s1_len], 0) + 1
        if s1_freq == s2_freq:
            return True
        else:
            return False
