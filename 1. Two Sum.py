def twoSum(nums, target): #nums = N, target = T
	seen = dict() #O(N) space
        found = False

        while not found:
            for i in range(len(nums)): #0(N) time
                otherNum = target - nums[i]
                if otherNum not in seen:
                    seen[nums[i]] = i
                else:
                    output = [i, seen[otherNum]]
                    found = True
        
        return output

nums = [3, 3]
target = 6
print(twoSum(nums, target))

#Time = O(N), Space = O(N)
