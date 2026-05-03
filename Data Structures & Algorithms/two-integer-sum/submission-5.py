class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {}
        
        for i, num in enumerate(nums):
            diff = target - num

            if diff in index_dict:
                return [index_dict[diff], i]

            index_dict[num] = i


            
        