# 算法

```python
import pandas as pd
import numpy as np

xx = pd.DataFrame(np.zeros((9,9)))

a = [0,1,2,3,4,5,6,7,8]

# 遍历所有的格子
for i in range(len(a)):
    for j in range(len(a)):
        xx.iloc[i][j] = 2
```

```python
xx = pd.DataFrame(np.zeros((9,9)))

# 遍历所有的格子
for i in range(len(a)):
    for j in range(i,len(a)):
        xx.iloc[i][j] = 2
```


```python
xx = pd.DataFrame(np.zeros((9,9)))

# 遍历所有的格子
for i in range(len(a)):
    for j in range(i):
        xx.iloc[i][j] = 2
```

```python
xx = pd.DataFrame(np.zeros((9,9)))

# 遍历所有的格子
for i in range(len(a)):
    for j in range(len(a)):
        if i == j:
            xx.iloc[i][j] = 2
```

```python

class Core:
    def __init__(self,left,right):
        self.left = left
        self.right = right
        
    def __lt__(self,other):
        print('小于')
        return True
    
    def __gt__(self,other):
        print('大于')
        return False
    
    def __eq__(self,other):
        print('等于')
        return True


a = Core(1,2)
b = Core(2,3)

a==b

a>b

```

```python
def binary_search(nums: list[int], target: int) -> int:
    """二分查找（双闭区间）"""
    # 初始化双闭区间 [0, n-1] ，即 i, j 分别指向数组首元素、尾元素
    i, j = 0, len(nums) - 1
    # 循环，当搜索区间为空时跳出（当 i > j 时为空）
    while i <= j:
        # 理论上 Python 的数字可以无限大（取决于内存大小），无须考虑大数越界问题
        m = (i + j) // 2  # 计算中点索引 m
        if nums[m] < target:
            i = m + 1  # 此情况说明 target 在区间 [m+1, j] 中
        elif nums[m] > target:
            j = m - 1  # 此情况说明 target 在区间 [i, m-1] 中
        else:
            return m  # 找到目标元素，返回其索引
    return -1  # 未找到目标元素，返回 -1

```


插入排序

折半插入排序

希尔排序




概念
维护一个窗口  有左右两个指针
扩大和缩小窗口


性质
基本用于数组或字符串问题, 解决子数组或子串相关的问题
通常可以将时间复杂度从 n方 优化到 n
