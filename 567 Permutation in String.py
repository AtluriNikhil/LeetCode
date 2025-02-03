# Solution 1
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

# Solution 2
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2:
            return False

        s1_counts = [0] * 26
        s2_counts = [0] * 26

        for i in range(n1):
            s1_counts[ord(s1[i]) - 97] += 1
            s2_counts[ord(s2[i]) - 97] += 1

        if s1_counts == s2_counts:
            return True

        for i in range(n1, n2):
            s2_counts[ord(s2[i]) - 97] += 1
            s2_counts[ord(s2[i - n1]) - ord("a")] -= 1
            if s1_counts == s2_counts:
                return True

        return False
