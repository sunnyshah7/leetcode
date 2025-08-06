class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        unique_ele = 0
        if nums[0] == 0:
            unique_ele = -1
            
        for i in range(1,len(nums)):
            if nums[i] == 0:
                continue
            else:
                unique_ele += 1
                nums[unique_ele] = nums[i]
                
                if unique_ele != i:
                    nums[i] = 0
        