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

# Solution 2
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        pq = []
        for key, value in freq.items():
            pq.append((-value, key))
        heapq.heapify(pq)
        result = []
        while k > 0:
            val = heapq.heappop(pq)[1]
            result.append(val)
            k -= 1
        return result
