import random
import math
#from main import *

matrix = []
# 生成一个随机的数组
def get_random_unit():
    _num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(_num_list)#随机打乱序列顺序
    return _num_list

#打印出矩阵arr中的每一列
def print_grid(arr):
    for i in range(9):
        print(arr[i])

#得到这行里已经用过的数
def get_row(row):
    row_arr = []
    for v in matrix[row]:
        if v == 0:
            continue
        row_arr.append(v)
    return row_arr

#得到这列里已经用过的数
def get_col(col):
    col_arr = []
    for i in range(9):
        val = matrix[i][col]
        if val == 0:
            continue
        col_arr.append(matrix[i][col])
    return col_arr

#得到这个宫已经用过的数
def get_block(num):
    col_arr = []
    seq = num % 3
    col_end = 9 if seq == 0 else seq * 3
    row_end = int(math.ceil(num / 3) * 3)
    for i in range(row_end - 3, row_end):
        for j in range(col_end - 3, col_end):
            val = matrix[i][j]
            if val != 0:
                col_arr.append(matrix[i][j])
    return col_arr

#得到所在的第几宫（1到9）
def get_block_seq(row, col):
    col_seq = int(math.ceil((col + 0.1) / 3))#进1取整
    row_seq = int(math.ceil((row + 0.1) / 3))
    return 3 * (row_seq - 1) + col_seq

#获取可能的填入的数
def get_enable_arr(row, col):
    avail_arr = get_random_unit()#得到乱序的1到9
    seq = get_block_seq(row, col)#得到所起的宫号（1到9）
    block = get_block(seq)
    row = get_row(row)
    col = get_col(col)
    unable_arr = list(set(block + row + col))
    for v in unable_arr:
        if v in avail_arr:
            avail_arr.remove(v)#把不可能填入的数排出去
    return avail_arr
def createSD():
    can_num = {}#
    # 初始化一个9行9列的数组，初值都为0
    for i in range(9):
        matrix.append([0] * 9)

    
    #保存还未填入数字的空格的位置
    box_list = []
    for row in range(9):
        for col in range(9):
            if matrix[row][col] == 0:
                box_list.append({'row': row, 'col': col})

    i = 0
    while i < len(box_list):   #未填满时循环
        position = box_list[i]#用i来读取未填入数字的位置表示的字典
        row = position['row']
        col = position['col']
        key = '%dx%d' % (row, col)
        #print(key)
        if key in can_num:
            enable_arr = can_num[key]
        else:
            enable_arr = get_enable_arr(row, col)
            can_num[key] = enable_arr #以位置为键可能放入的数列表为值存入字典
        if len(enable_arr) <= 0:#没有可填入数字时，回退一个格子在重新新选入一个新的可能值填入
            i -= 1                 
            if key in can_num:     
                del (can_num[key])
            matrix[row][col] = 0
            continue  #结束本次循环
        else:
            matrix[row][col]= enable_arr.pop()#从可能数字中探出最后一个填入
            i += 1
    return matrix
