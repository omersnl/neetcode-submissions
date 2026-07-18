class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        counter = {}

        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        
        for num, cnt in counter.items():
            freq[cnt].append(num)
        
        for i in range(len(freq) - 1, -1, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

