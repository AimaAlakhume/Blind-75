def twoSum(nums, target): #nums = N, target = T
        """
        iterate through the array
            subtract the curr num from target num
            if diff in seen:
                return curr num ind and seen[diff]
            add curr num to seen with ind as val
        """
        seen = dict()

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            seen[nums[i]] = i

nums = [3, 3]
target = 6
print(twoSum(nums, target))

#Time = O(N), Space = O(N)
