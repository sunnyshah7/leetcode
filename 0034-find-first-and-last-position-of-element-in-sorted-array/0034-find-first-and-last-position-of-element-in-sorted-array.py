class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def first_occurrence(nums, target):
            ans = -1
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (s + e) // 2
                if nums[mid] == target:
                    ans = mid 
                    e = mid - 1 
                elif nums[mid] < target:
                    s = mid + 1
                else:
                    e = mid - 1
            return ans

        def last_occurrence(nums, target):
            ans = -1
            s, e = 0, len(nums) - 1
            while s <= e:
                mid = (s + e) // 2
                if nums[mid] == target:
                    ans = mid 
                    s = mid + 1 
                elif nums[mid] < target:
                    s = mid + 1
                else: 
                    e = mid - 1
            return ans

        first = first_occurrence(nums, target)
        last = last_occurrence(nums, target)
        return [first, last]