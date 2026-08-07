class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dict = {}

        for c in s:
            s_dict[c] = s_dict.get(c, 0) + 1

        for c in t:
            if c not in s_dict or s_dict[c] == 0:
                return False
            else:
                s_dict[c] -= 1
        
        return True

            