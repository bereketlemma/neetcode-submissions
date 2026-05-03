class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return list(anagrams.values())
    # Complexity Analysis for worst Case senario:
    # N- Number of total strings:6
    # K- length of the string:4
    # for each sorting: O(N*k*logk)=O(6*4*log4)=6*4*2= 48 operations

    # Space complexity:O(N*K)=O(6*4)=O(24)



        