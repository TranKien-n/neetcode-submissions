class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        start, end = 0, len(nums) - 1

        while start <= end:
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break

            mid = (start + end) // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[start]:
                start = mid + 1
            elif nums[mid] < nums[start]:
                end = mid - 1
        
        smallest_index = nums.index(res)
        print(smallest_index)
        start, end = 0, smallest_index - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                return mid
        
        start, end = smallest_index, len(nums) - 1

        while start <= end:
            mid = (start + end) // 2

            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            elif nums[mid] == target:
                return mid
        
        return -1


        