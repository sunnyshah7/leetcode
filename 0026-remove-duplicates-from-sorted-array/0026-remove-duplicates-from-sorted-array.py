class Solution(object):
    def removeDuplicates(self, nums):
        i = 0
        for j in range(0,len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1

        
        