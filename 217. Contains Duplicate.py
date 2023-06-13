def containsDuplicate(nums):

    numsSet = set() #O(1) time, O(n) space

    for i in range(len(nums)): #O(n) time, O(1) space
        numsSet.add(nums[i])

    if len(numsSet) == len(nums): #O(1) time, O(1) space
        return False
    else:
        return True

 #space: O(n), time: O(n)
