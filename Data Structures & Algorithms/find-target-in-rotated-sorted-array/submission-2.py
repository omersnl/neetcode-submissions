class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            elif target == nums[l]:
                return l
            elif target == nums[r]:
                return r
            
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1  # target in left half
                else:
                    l = mid + 1  # target in right half
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1  # target in right half
                else:
                    r = mid - 1  # target in left half

        return -1

            