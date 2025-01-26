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
# Uses a dictionary where each key represents a number from the input array, and its corresponding value indicates the length of a consecutive sequence with that number as either the upper or lower bound of the sequence.
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        table = {}
        maxval = 0
        for num in nums:
            x = table.get(num - 1, 0)
            y = table.get(num + 1, 0)
            val = x + y + 1
            table[num - x] = val
            table[num + y] = val
            maxval = max(maxval, val)
        return maxval
