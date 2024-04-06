s=int(input("输入行列式："))
mat=[]
import itertools
import math
import time
t1=time.time()
for i in range(s):
    arr=input().split()
    for j in range(len(arr)):
        arr[j]=int(arr[j])
    mat.append(arr)
#输入行列式
def judge(l):
    step=0
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                step+=1
    if step%2==0:
        return 1
    else:
        return -1
#奇偶序列判定
numbers= list(range(s))
lb=list(itertools.permutations(numbers))
#生成全排列
su=0
for i in range(math.factorial(s)):
    pro=1
    samp=lb[i]
    for j in range(len(samp)):
        u=samp[j]
        elem=mat[j][u]
        pro=pro*elem
    prod=pro*judge(samp)
    su=su+prod
t2=time.time()
t=t2-t1
print("矩阵的值为:",su,"用时:",t)
time.sleep(3600)

    
    
