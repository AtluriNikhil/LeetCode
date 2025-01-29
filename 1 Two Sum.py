class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        parsedNumbers = dict()
        for index in range(len(nums)):
            if target - nums[index] in parsedNumbers:
                return [index, parsedNumbers[target - nums[index]]]
            else:
                parsedNumbers[nums[index]] = index
