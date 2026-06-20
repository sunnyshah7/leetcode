class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count_dict = {}
        n = len(nums)
        remaining = 0
        for i in range(0,n):
            remaining = target - nums[i]
            if remaining in count_dict:
                return [count_dict[remaining],i]
            count_dict[nums[i]] = i