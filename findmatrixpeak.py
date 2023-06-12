def find_global_peak(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    def find_max_in_col(col):
        max_val = float('-inf')
        max_row = 0
        for i in range(rows):
            if matrix[i][col] > max_val:
                max_val = matrix[i][col]
                max_row = i
        return max_row, max_val

    def find_peak_in_matrix(start_col, end_col):
        mid_col = (start_col + end_col) // 2
        max_row, max_val = find_max_in_col(mid_col) # 找到中间列的最大值

        if (mid_col == 0 or max_val >= matrix[max_row][mid_col-1]) and (mid_col == cols-1 or max_val >= matrix[max_row][mid_col+1]): # 如果是峰值
            return max_val
        elif mid_col > 0 and matrix[max_row][mid_col-1] > max_val: # 如果左边有更大的值
            return find_peak_in_matrix(start_col, mid_col-1)
        else:
            return find_peak_in_matrix(mid_col+1, end_col)

    return find_peak_in_matrix(0, cols-1)

# 示例用法
matrix = [
    [1, 3, 5, 4],
    [8, 6, 9, 7],
    [3, 2, 8, 1],
    [5, 4, 6, 2]
]

peak = find_global_peak(matrix)
if peak is not None:
    print("找到峰值：", peak)  #这只是一个峰值，不一定是全局峰值，峰值的定义是比上下左右都大，所以他就会是一个峰值，实际上这个矩阵有两个峰值，一个是9，一个是8
else:
    print("矩阵中没有峰值。")
