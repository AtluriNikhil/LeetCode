# Optimal Solution

class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left_product = [0] * n
        right_product = [0] * n
        l_product = 1
        r_product = 1

        for i in range(n):
            j = -i-1
            left_product[i] = l_product
            right_product[j] = r_product
            l_product *= nums[i]
            r_product *= nums[j]

        return [left_product[i]*right_product[i] for i in range(n)]

# Solution 1
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_mult_array = [1]
        suffix_mult_array = [1]
        product = 1
        for num in nums:
            product = product * num
            prefix_mult_array.append(product)
            
        product = 1
        for num in nums[::-1]:
            product = product * num
            suffix_mult_array.insert(0, product)

        result = list()
        for index in range(len(nums)):
            result.append(prefix_mult_array[index] * suffix_mult_array[index+1])
        return result

# Solution 2
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]
        length = len(nums)
        product = 1
        for num in nums:
            product = product * num
            result.append(product)

        product = 1
        for index in range(length-1, -1, -1):
            product = product*nums[index]
            nums[index] = product
        nums.append(1)

        result.pop()
        nums.pop(0)

        for index in range(length):
            result[index] = result[index] * nums[index]
        return result
