class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            start = 0
            end = len(matrix[i]) - 1
            found = False

            while start <= end:
                mid = (start + end) // 2
                print(i, mid)
                num = matrix[i][mid]

                if target < num:
                    end = mid - 1
                elif target > num:
                    start = mid + 1
                elif target == num:
                    found = True
                    return found
        
        return False