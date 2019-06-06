from createFun import *
#createSD()

def isSD(mat):
    TS="是正确的数独矩阵!"  #提示消息
    flag=True
    for i in range(9):
        for j in range(9):#双循环遍历矩阵
            
            if mat[i][j]==0: #有等于0的数说明，还有格子没有填入数字
                flag=False
                TS="输入有误！还有未填入数字！"
                return flag,TS
            elif mat[i][j] not in [1,2,3,4,5,6,7,8,9]:
                flag=False
                TS="输入有误！请填入到1到9的数字！"
                return flag,TS
            n=0      #记录mat[i][j]出现的次数
            g_num=get_block_seq(i,j)#得到所在的宫号
            g_arr=get_block(g_num)  #得到这个宫已经用过的数字
            #print(g_num,g_arr)
            for k in g_arr:        #遍历宫里的数字，统计同宫mat[i][j]的个数
                if mat[i][j]==k:
                    n+=1
            for x in range(9):
                if mat[i][j]==mat[i][x]:#统计同行mat[i][j]的个数
                    n+=1
                if mat[i][j]==mat[x][j]:#统计同列mat[i][j]的个数
                    n+=1
            if n>3:     #为什么是3？从行、列、宫里都数了一次这个数
                flag=False
                TS="输入有误！同宫、同行、同列的"+str(mat[x][j])+"总个数有："+str(n)+"个"
    return flag,TS
#isSD(matrix)
