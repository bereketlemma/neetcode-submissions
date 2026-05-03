class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check_duplicate = set()
        for n in nums:
            if n in check_duplicate:
                return True
            check_duplicate.add(n)
        return False