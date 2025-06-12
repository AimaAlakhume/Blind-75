class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        """
        create a new array
        iterate through nums//2
            append nums[i]
            append nums[i+n]
        return new array
        """

        output_arr = []
        for i in range(n):
            output_arr.append(nums[i])
            output_arr.append(nums[i+n])
        return output_arr
