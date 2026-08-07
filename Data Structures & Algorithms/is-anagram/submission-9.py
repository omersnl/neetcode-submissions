class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_dict = Counter(s)

        for c in t:
            if s_dict[c] == 0:
                return False
            else:
                s_dict[c] -= 1
        
        return True

            