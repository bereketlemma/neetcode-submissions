class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Bruteforce way of solving this problem
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    # Found Duplicate
                    return True
        # Unique Value
        return False
# Time Comp: O(n^2)
# Space:O(n^2)
        