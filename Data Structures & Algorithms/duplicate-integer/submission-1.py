class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Store_duplicate = set()
        for num in nums:
            if num in Store_duplicate:
                return True
            Store_duplicate.add(num)
        return False
         