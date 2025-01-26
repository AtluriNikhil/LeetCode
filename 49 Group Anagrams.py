# Solution 1

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strings_array = list()
        for index in range(len(strs)):
            # Cannot directly sort the strings be carful about this step
            sorted_strings_array.append([''.join(sorted(strs[index])), index])
        sorted_strings_array = sorted(sorted_strings_array,key=lambda x: x[0])
        result = list()
        matched_string = None
        for string_elem in sorted_strings_array:
          # I am doing this here as the above sorted gives me back the list of chars instead of string directly
          # sorted_strings_array.append([''.join(sorted(strs[index])), index])
          # this line is what causes issue
            if matched_string == ''.join(string_elem[0]):
                result[-1].append(strs[string_elem[1]])
            else:
                result.append([strs[string_elem[1]]])
                matched_string = ''.join(string_elem[0])
        return result

# Solution 2
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagram_map[sorted_word].append(word)
        return list(anagram_map.values())
