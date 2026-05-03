class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # using built in python function Counter 
        # return Counter(t) == Counter(s)
        return sorted(t) == sorted(s)