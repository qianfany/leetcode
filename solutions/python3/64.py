from typing import List

"""
Explanation:

We first get the dimensions of the input grid using m = len(grid) and n = len(grid[0]).
We then initialize the first row and first column of the grid by adding up the previous element's value. This is because there is only one path to reach each of these cells.
Next, we loop through the rest of the cells of the grid (excluding the first row and column) and compute the minimum path sum for each cell using dynamic programming. We update each cell with the sum of its own value and the minimum value from the cells above and to the left of it.
Finally, we return the value in the last cell of the grid, which represents the minimum path sum from the top left to the bottom right corner of the grid.
Note: This solution has a time complexity of O(m*n) and a space complexity of O(1), where m and n are the dimensions of the input grid.

Step 1:            Step 2:            Step 3:            Step 4:
 1  3  1             1  4  5             1  4  5             1  4  5
 1  5  1     ->      2  0  0             2  7  6             2  7  6
 4  2  1             6  0  0             6  8  7             6  8  7

"""
def min_path_sum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    # initialize the first row and column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    # dynamic programming to fill the rest of the grid
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    return grid[-1][-1]


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] += min(grid[i][j - 1] if j > 0 else float("inf"), grid[i - 1][j] if i > 0 else float("inf")) if i!=0 or j != 0 else 0
        return grid[-1][-1]


if __name__ == '__main__':
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    zhushi = Solution()
    print(zhushi.minPathSum(grid))
    print(min_path_sum(grid))
