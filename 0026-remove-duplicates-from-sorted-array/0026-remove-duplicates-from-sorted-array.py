class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_ele = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
               unique_ele += 1
               nums[unique_ele] = nums[i]
            else:
                continue
                
        return unique_ele + 1        

