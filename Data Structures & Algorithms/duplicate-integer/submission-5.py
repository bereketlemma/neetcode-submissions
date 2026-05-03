class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checkDuplicate = set()
        for num in nums:
            if num in checkDuplicate:
                return True
            checkDuplicate.add(num)
        return False
        # nums.sort()
        # for num in range(1, len(nums)):
        #     if nums[num] == nums[num-1]:
        #         return True
        # return False
        # Given problem desc:
        # Input: array[nums]-int
        # Output: true or False
        # True: found Duplicate 
        # False: no duplicate if all Unique 
    
        # Scoping:
        # What will happen if we have morethan one Duplicate?
        # Example:nums:[1,2,3,2,1]
        # in this case we have 1 repeated 2x and 2 repeated 2x?
        # Return True 
        # What if i have empty array->False
        # The array can also have both negative and positive number
          
        # Bruteforce and Pseudo 

        # Approach 1:Using Hashmap
        # Using a hashmap and mapping every value with its frequency:
        # Value : Frequency-{ 1:1, 2:1 , 3:2}
        # Return True because we found duplicate if not return False
        # Time complexity : O(n)
        # space Complexity : O(n)

        # Approach 2 : Sorting the numbers in order the counting each of them
        # Efficiency depends on what sorting algo we are using:
        # in most cases : Time: O(nlogn)
        # Space: O(n) or O(1) it depends 



         