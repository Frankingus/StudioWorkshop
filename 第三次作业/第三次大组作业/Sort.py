import random
import time
from telnetlib import OLD_ENVIRON


def InsertTime(arr):
    Len = str(len(arr))
    start = time.time()
    Insert_Sort(arr,len(arr))
    end = time.time()
    print('插入排序' + Len + '个数所需时间:' + str(round(end - start,2)) + '秒')

def MergeTime(arr):
    Len = str(len(arr))
    start = time.time()
    Merge_Sort(arr, len(arr))
    end = time.time()
    print('归并排序' + Len + '个数所需时间:' + str(round(end - start,2)) + '秒')

def QuickTime(arr):
    Len = str(len(arr))
    start = time.time()
    Quick_Sort(arr, len(arr))
    end = time.time()
    print('快速排序' + Len + '个数所需时间:' + str(round(end - start, 2)) + '秒')

def CountTime(arr):
    Len = str(len(arr))
    start = time.time()
    Count_Sort(arr, len(arr))
    end = time.time()
    print('计数排序' + Len + '个数所需时间:' + str(round(end - start, 2)) + '秒')

def RadixCountTime(arr):
    Len = str(len(arr))
    start = time.time()
    RadixCount_Sort(arr, len(arr))
    end = time.time()
    print('基数排序' + Len + '个数所需时间:' + str(round(end - start, 2)) + '秒')

def InsertTime100(arr):
    start = time.time()
    for i in range(100):
        Insert_Sort(arr,len(arr))
    end = time.time()
    print('插入排序1000个数100次所需时间:' + str(round(end - start,2)) + '秒')

def MergeTime100(arr):
    start = time.time()
    for i in range(100):
        Merge_Sort(arr, len(arr))
    end = time.time()
    print('归并排序1000个数100次所需时间:' + str(round(end - start,2)) + '秒')

def QuickTime100(arr):
    start = time.time()
    for i in range(100):
        Quick_Sort(arr, len(arr))
    end = time.time()
    print('快速排序1000个数100次所需时间:' + str(round(end - start, 2)) + '秒')

def CountTime100(arr):
    start = time.time()
    for i in range(100):
        Count_Sort(arr, len(arr))
    end = time.time()
    print('计数排序1000个数100次所需时间:' + str(round(end - start, 2)) + '秒')

def RadixCountTime100(arr):
    start = time.time()
    for i in range(100):
        RadixCount_Sort(arr, len(arr))
    end = time.time()
    print('基数排序1000个数100次所需时间:' + str(round(end - start, 2)) + '秒')


def Insert_Sort(Old : list[int], n : int) -> list[int]:
    New = []
    imin = 0
    while Old:
        for i in range(0,n):
            if Old[i] < Old[imin]:
                imin = i
        New.append(Old.pop(imin))
        imin = 0
        n -= 1
    return New


def MergeDetail(Left : list[int],Right : list[int]) -> list[int]:
    New = []
    if len(Left) > 1:
        Left = MergeDetail(Left[:(len(Left)-1)//2+1],Left[(len(Left)-1)//2+1:])
    if len(Right) > 1:
        Right = MergeDetail(Right[:(len(Right) - 1) // 2 + 1], Right[(len(Right) - 1) // 2+1:])
    while Left and Right:
        if Left[0] <= Right[0]:
            New.append(Left.pop(0))
        else:
            New.append(Right.pop(0))
    while Left:
        New.append(Left.pop(0))
    while Right:
        New.append(Right.pop(0))
    return New

def Merge_Sort(Old : list[int], n : int) -> list[int]:
    if n == 1:
        return Old
    else:
        return MergeDetail(Old[:(n-1)//2+1],Old[(n-1)//2+1:])

def QuickDetail(Old : list[int]):
    if len(Old) > 2:
        L = 0 #左指针
        R = -1 #右指针
        flag = 1 #1左往右，0右往左
        Temp = Old[-1]
        TempS = -1 #基准数
        while L + (0-R) != len(Old):
            if flag == 1:
                if Old[L] > Temp:
                    Old[TempS] = Old[L]
                    TempS = L
                    flag = 0
                else:
                    L += 1
            elif flag == 0:
                if Old[R] < Temp:
                    Old[TempS] = Old[R]
                    TempS = R
                    flag = 1
                else:
                    R -= 1
        Old[TempS] = Temp
        if TempS == 0:
            Left = []
            Right = QuickDetail(Old[TempS + 1:])
        elif TempS == -1:
            Left = QuickDetail(Old[:TempS])
            Right = []
        else:
            Left = QuickDetail(Old[:TempS])
            Right = QuickDetail(Old[TempS + 1:])
        Left.append(Temp)
        return Left + Right
    elif len(Old) == 2:
        if Old[0] > Old[1]:
            New = [Old[1],Old[0]]
        else:
            New = Old
        return New
    else:
        return Old

def Quick_Sort(Old: list[int], n: int) -> list[int]:
    New = QuickDetail(Old)
    return New

def Count_Sort(Old: list[int], n: int) -> list[int]:
    max = -114514
    for i in Old:
        if i > max:
            max = i
    jishu = []
    if max >= n:
        jishu = [0] * (max+1)
    else:
        jishu = [0] * n
    while Old:
        jishu[Old.pop(0)] += 1
    New = []
    for i,item in enumerate(jishu):
        if item >= 1:
            while item != 0:
                New.append(i)
                item -= 1
    return New



def RadixCount_Sort(Old: list[int], n: int) -> list[int]:
    mnum = max(Old)
    New = []
    cnt = 0
    exp = 1
    while mnum != 0:
        mnum = mnum // 10
        for i in range(10):
            for j in Old:
                if j//exp%10 == i:
                    New.append(j)
        Old = New[:]
        New = []
        exp += 1
    return Old




#生成数组
random.seed(0)
test = list(range(99999999))
t1w = random.sample(test,10000)
t5w = random.sample(test,50000)
t20w = random.sample(test,200000)
t1k = random.sample(test,1000)

num1 = int(input('10000个：1\n50000个：5\n200000个：20\n1000个100次：1010\n请输入数组长度:'))
num2 = int(input('插入排序：1\n归并排序：2\n快速排序：3\n计数排序：4\n基数排序：5\n请选择排序方式:'))
tw = []
if num1 == 1:
    tw = t1w[:]
elif num1 == 5:
    tw = t5w[:]
elif num1 == 20:
    tw = t20w[:]
elif num1 == 1010:
    tw = t1k[:]

if num1 != 1010:
    if num2 == 1:
        InsertTime(tw)
    elif num2 == 2:
        MergeTime(tw)
    elif num2 == 3:
        QuickTime(tw)
    elif num2 == 4:
        CountTime(tw)
    elif num2 == 5:
        RadixCountTime(tw)
else:
    if num2 == 1:
        InsertTime100(tw)
    elif num2 == 2:
        MergeTime100(tw)
    elif num2 == 3:
        QuickTime100(tw)
    elif num2 == 4:
        CountTime100(tw)
    elif num2 == 5:
        RadixCountTime100(tw)


# b = [2,5,3,7,114514,6,8,1,1,2]
# Sortb = RadixCount_Sort(b,len(b))
# print(Sortb)

#插入排序：1w->2.32s ; 5w->73.67s ; 20w->2221.92s ; 1000个100次->0.03s
#归并排序：1w->0.08s ; 5w->2.63s ; 20w->42.22s ; 1000个100次->0.14s
#快速排序：1w->0.04s ; 5w->0.16s ; 20w->0.97s ; 1000个100次->0.33s
#计数排序：1w->4.74s ; 5w->7.45s ; 20w->46.58s ; 1000个100次->4.15s
#基数排序：1w->0.05s ; 5w->0.25s ; 20w->1.29s ; 1000个100次->0.51s
