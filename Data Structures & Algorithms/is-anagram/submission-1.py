class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # The two strings are not anagram if the len is not the same
        if len(t) != len(s):
            return False
        return sorted(s) == sorted (t)
# Time Complex : for length : O(t) + O(s)
# Time Complex : for Sorting : O(logt) + O(logs)
# Time Complex : Overall : O(tlogt) + O(slogs)
# Depeding on the sorting Algo used
