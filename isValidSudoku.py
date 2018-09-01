# -*- coding: utf-8 -*-
__author__ = "PANGHENGTAO"
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        sum1 = [[-1 for x in range(9)] for y in range(9)]
        sum2 = [[-1 for x in range(9)] for y in range(9)]
        sum3 = [[-1 for x in range(9)] for y in range(9)]

        for x in range(9):
            for y in range(9):
                if board[x][y] != '.':
                    num = int(board[x][y]) - 1
                    k = x // 3 + (y // 3) * 3
                    print(x, y, num)
                    print('sum = ', sum1[x][num], sum2[y][num], sum3[k][num])
                    
                    if sum1[x][num] == 1 or sum2[y][num] == 1 or sum3[k][num] == 1:
                        return False
                    sum1[x][num] = 1
                    sum2[y][num] = 1
                    sum3[k][num] = 1
        return True


src = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
a = s.isValidSudoku(src)
print(a)