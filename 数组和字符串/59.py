from typing import List
class Solution1:
    def generateMatrix(self, n: int) -> List[List[int]]:

        #每次都是右下左上
        #⭐左闭右开，因为每次最后一个会跟下一次第一个重复，左闭右开正好接上
        mat=[[0]*n for _ in range(n)] #生成n*n的全0矩阵
        count=1 #从1开始填数
        start_index=0 #标记当前循环的初始位置（填到了哪一圈），初始化为0，即第一圈填的(0,0)这个位置
        while not count>=n**2:
            for j in range(start_index,n-1-start_index): #右
                mat[start_index][j]=count
                count+=1
            
            for i in range(start_index,n-1-start_index): #下
                mat[i][n-1-start_index]=count
                count+=1
            
            for j in range(n-1-start_index,start_index,-1): #左
                mat[n-1-start_index][j]=count
                count+=1
            
            for i in range(n-1-start_index,start_index,-1): #上
                mat[i][start_index]=count
                count+=1
            start_index+=1

            '''不加start_index例子，帮助理解
            for j in range(n-1): #右
                mat[0][j]=count
                count+=1
            
            for i in range(0,n-1): #下
                mat[i][n-1]=count
                count+=1
            
            for j in range(n-1,0,-1): #左
                mat[n-1][j]=count
                count+=1
            
            for i in range(n-1,0,-1): #上
                mat[i][0]=count
                count+=1
            start_index+=1
            '''

        if n%2==1:#n为奇数时最后一个数会漏填
            mat[n//2][n//2]=count
            
        return mat

class Solution2:
    def generateMatrix(self, n: int) -> List[List[int]]:\
        #边界收缩法/撞墙法
        #⭐看到矩阵奇怪的遍历方式（非按行按列遍历）就要想到
        #让边界成为四堵墙，top，bottom，left，right
        #依旧是右下左上
        #----------------------------------------
        #右最终会撞到right说明top行填完，top下移
        #下最终会撞到bottom说明right列填完，right左移
        #左最终会撞到left说明bottom行填完，bottom上移
        #上最终会撞到top说明left列填完，left右移
        mat=[[0]*n for _ in range(n)]

        top,bottom=0,n-1
        left,right=0,n-1
        count=1

        while count<=n**2:
            for j in range(left,right+1): #右
                mat[top][j]=count
                count+=1
            top+=1

            for i in range(top,right+1):#下
                mat[i][right]=count
                count+=1
            right-=1

            for j in range(right,left-1,-1):#左
                mat[bottom][j]=count
                count+=1
            bottom-=1

            for i in range(bottom,top-1,-1): #上
                mat[i][left]=count
                count+=1
            left+=1

        return mat
            


if __name__=="__main__":
    s=Solution1()
    s.generateMatrix(4)