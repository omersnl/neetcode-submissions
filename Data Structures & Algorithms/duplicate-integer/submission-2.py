class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = []

        for n in nums:
            if n in seen:
                return True
            elif n not in seen:
                seen.append(n)
        
        return False
