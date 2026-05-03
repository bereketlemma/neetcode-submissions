class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            diff = target - nums[i] 
            if diff in seen:
                return[nums.index(diff), i]
            seen.add(nums[i])


        