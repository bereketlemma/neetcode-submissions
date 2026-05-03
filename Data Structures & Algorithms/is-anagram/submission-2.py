
from collections import Counter 
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S_dict = Counter(s)
        T_dict = Counter(t)
        return S_dict == T_dict

        