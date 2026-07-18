class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count_dict = {}
        res = 0

        maxf = 0

        for r in range(len(s)):
            count_dict[s[r]] = 1 + count_dict.get(s[r], 0)
            maxf = max(maxf, count_dict[s[r]])

            while (r - l + 1) - maxf > k:
                count_dict[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res
            