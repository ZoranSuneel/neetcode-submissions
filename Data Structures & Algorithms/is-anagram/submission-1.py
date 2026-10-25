class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        x = list(s)
        y = list(t)
        if len(x) != len(y):
            return False
        
        return sorted(x)==sorted(y)