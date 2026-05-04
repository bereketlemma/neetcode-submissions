class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # What we can do pick a consecutative number and return the maximum sum
        # If it is only one number it is going to be it's self
        # For exmple we are given -2,7,-3,4 
        # That is going to be 8 
        # So the approach we followed is Bottom up appraoch Dynamic programing and it is constant space 
        # Feels like greddy but can be called anyone
        # We need to keep 2 variables: cur_sum = 0 and max_sum set to negative infnity because we can have negative values 
        # Like we see in the first example it starts with -2 which is better than negative infinity 
        # So that we set the maxsum to -2 because so far that is the best we have and it is better than - inf 
        # when finding the maximum subarray it is better to use zero value anytime we see negative and go to the next one
        # So far we hav cur_sum set to zero and max_sum set to -2
        # next one value is 7 so we change curr sum set to 7 and we keep it and move to next one which is -3
        # we can't skip the negative here because after that we have positive number and we are looking at the overall sum
        # we still keep it and curr sum is 4 and max sum is 4
        # then we find 4 and now we have curr_sum is 8 and max_sum 8
        # So the logic is basically if you loop the nums and curr sum is lesstahn zero set it to zero and move 
        # if it positive number we will keep that because it contributes
        import math 

        max_sum = -math.inf
        curr_sum = 0

        for i in range(len(nums)):
            # go up by thr value we are lookin up
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)

            if curr_sum < 0:
                curr_sum = 0
        return max_sum

        # Time: O(N)
        # Space: O(N)




 
        