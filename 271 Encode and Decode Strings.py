class Solution:
    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result = result + str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        index = 0
        result = []
        while index < len(s):
            length = ""
            while s[index] != "#":
                length = length + s[index]
                index += 1
            length = int(length)
            result.append(s[index + 1 : index + 1 + length])
            index = index + 1 + length
        return result
