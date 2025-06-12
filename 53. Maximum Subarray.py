class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        highest_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            curr_num = nums[i]
            curr_sum = max(curr_num, curr_sum + curr_num)
            highest_sum = max(highest_sum, curr_sum)

        return highest_sum
