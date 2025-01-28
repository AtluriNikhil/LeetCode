# Solution 1
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        result = 1
        count = 1
        prev_value = nums[0]
        for num in nums[1:]:
            if prev_value + 1 == num:
                count = count + 1
                prev_value = num
            elif prev_value == num:
                pass
            else:
                if count > result:
                    result = count
                count = 1
                prev_value = num
        if count > result:
            return count
        return result

# Solution 2
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                length = 1
                while num + length in nums:
                    length += 1
                if length > longest:
                    longest = length
        return longest
