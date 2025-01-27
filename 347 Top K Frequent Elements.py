# Solution 1
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1

        frequency = set(sorted(hashMap.values(), reverse = True)[:k])

        result = []
        for key, value in hashMap.items():
            if value in frequency:
                result.append(key)

        return result
