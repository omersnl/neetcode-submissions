class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       s_dict = Counter(s)

       if len(s) != len(t):
        return False

       for char in t:
        if s_dict[char] > 0:
            s_dict[char] -= 1
        elif s_dict[char] == 0:
            return False
       return True

