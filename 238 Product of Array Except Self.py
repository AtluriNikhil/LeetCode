# Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult_array = [1]
        suffix_mult_array = [1]
        product = 1
        for num in nums:
            prefix_mult_array.append(product*num)
            product = product * num
        product = 1
        for num in nums[::-1]:
            suffix_mult_array.insert(0, product*num)
            product = product * num
        result = list()
        for index in range(len(nums)):
            result.append(prefix_mult_array[index] * suffix_mult_array[index+1])
        return result
