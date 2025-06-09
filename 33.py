class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Search algorithm with O(log n) complexity — use binary search
        # Given: Rotated sorted array, and a target number
        # Edge case: There may be no matching number

        # Binary search logic:
        # 1. Find which side is sorted
        # 2. Check if the sorted side contains the target
        #    - If it does, update l and r to narrow to that side
        #    - If not, update l and r to exclude that side
        # Repeat until l <= r

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m

            # Left side is sorted
            if nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            # Right side is sorted
            else:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
