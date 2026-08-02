class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        found = False
        
        while start <= end:
            mid = (end + start) // 2

            num = nums[mid]
            if num > target:
                end = mid - 1
                print(f"{num} < {target}")
            elif num < target:
                start = mid + 1
                print(f"{num}  {target}")
            elif num == target: 
                found = True
                break
        
        return mid if found else -1

