class Solution:
    def isPalindrome(self, s: str) -> bool:
        n_str = []

        for c in s:
            if c.isalnum():
                n_str.append(c)
        
        n_str = "".join(n_str).lower()

        l = 0
        r = len(n_str) - 1

        while l < r:
            if n_str[l] != n_str[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return True


    
    