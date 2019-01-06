# 介绍

这个仓库主要是算法课设的相关题目，主要包括tromino谜题、最大总和问题（数字三角形）、基因序列比较问题（最长公共字符串LCS问题）、地图着色问题（m图着色问题）。代码是基于python的。

# tromino谜题

主要使用分治算法以棋盘的中心为原点将棋盘划分成四个象限，然后不断地递归将棋盘划分成更小的棋盘直到棋盘的大小为2×2为止。

主要步骤如下：

1. 以棋盘的中心为原点将棋盘划分为四个象限分别为第一、第二、第三、第四象限，其中他们分别对应于笛卡尔坐标系中的第三、第二、第一、第四象限。
2. 判断缺块在哪个象限，并将原点周围除缺块存在的象限的三个方块覆盖上tromino。
3. 依次递归求解第一、第二、第三、第四象限并分别对子问题重复步骤（1）、（2）直到棋盘的大小为2×2为止递归结束。

伪代码如下：

```
算法 tromino(a, length, counter)
//tromino谜题算法
//a表示棋盘数组，length表示数组a的长度，counter表示计数器
i=length/2
if  i = 1
   if 缺块在第一象限
          二维数组的第二、三、四象限靠近原点的数组空间←counter++
   else if 缺块在第二象限
          二维数组的第一、三、四象限靠近原点的数组空间←counter++
   else if 缺块在第三象限
          二维数组的第一、二、四象限靠近原点的数组空间←counter++
   else
          二维数组的第一、二、三象限靠近原点的数组空间←counter++
   end if
else
   if 缺块在第一象限   
          二维数组的第二、三、四象限靠近原点的数组空间←counter++
          tromino(第一象限) //解第一象限
          tromino(第二象限) //解第二象限
          tromino(第三象限) //解第三象限
          tromino(第四象限) //解第四象限
   else if 缺块在第二象限
          二维数组的第一、三、四象限靠近原点的数组空间←counter++
          tromino(第一象限) //解第一象限
          tromino(第二象限) //解第二象限
          tromino(第三象限) //解第三象限
          tromino(第四象限) //解第四象限
  else if 缺块在第三象限
          二维数组的第一、二、四象限靠近原点的数组空间←counter++
          tromino(第一象限) //解第一象限
          tromino(第二象限) //解第二象限
          tromino(第三象限) //解第三象限
          tromino(第四象限) //解第四象限
  else  缺块在第四象限
          二维数组的第一、二、三象限靠近原点的数组空间←counter++
          tromino(第一象限) //解第一象限
          tromino(第二象限) //解第二象限
          tromino(第三象限) //解第三象限
          tromino(第四象限) //解第四象限
  end if
end if

```

# 最大总和问题

我们使用动态规划算法，把当前位置(i, j)看成一个状态，然后定义指标函数d(i, j)为从格子(i, j)出发的能得到的最大的和（包括其本身），我们以数塔的最后一层值为初始条件并从倒数第二层开始计算，那么本题就转化成了求d(1,1)。算法的状态转移方程如下所示：
{d_{(i,j)}}{\rm{  =  valu}}{{\rm{e}}_{(i,j){\rm{  +  }}}}\max \{ {d_{(i + 1,j)j}},{\rm{ }}{{\rm{d}}_{(i + 1,j + 1)}}\}

伪代码：

```
算法 MaximumSumProblem(value[l..n][1..n])
d = zeros(n, n)
for i←1 to n
    d[n][j] = value[n][i]
end
for i←n-1 to 1
    for j←1 to i
        d[i][j] = value[i][j] + max(d[i+1][j], d[i+1][j+1])
    end
end
return d

```



# 基因序列比较

我们动态规划算法比较序列AGTGATG和序列GTTAG具体步骤如下：

（1）我们根据相似度矩阵初始化得分矩阵, 首先建立下图中的得分矩阵。从第一列第一行的位置起始。

|      | A    | C    | G    | T    | -    |
| ---- | ---- | ---- | ---- | ---- | ---- |
| A    | 5    | -1   | -2   | -1   | -3   |
| C    | -1   | 5    | -3   | -2   | -4   |
| G    | -2   | -3   | 5    | -2   | -2   |
| T    | -1   | -2   | -2   | 5    | -1   |
| -    | -3   | -4   | -2   | -1   | *    |

<center>相似度矩阵</center>

|      |      | A    | G    | T    |      | A    | T    | G    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
|      |      | -3   | -2   | -1   | -2   | -3   | -1   | -2   |
| G    | -2   |      |      |      |      |      |      |      |
| T    | -1   |      |      |      |      |      |      |      |
| T    | -1   |      |      |      |      |      |      |      |
| A    | -3   |      |      |      |      |      |      |      |
| G    | -2   |      |      |      |      |      |      |      |

<center>初始化得分矩阵</center>

（2）首先我们确定状态转移方程
$$
F_{ij} = max of \left\{
\begin{array}{lr}
F_{i-1,j-1}+S(x_i, y_j)\qquad(左侧和上面的字符比对)\\
F_{i-1,j}+S(x_{i-1}, '-')\qquad(上面的字符和空格比对)\\
F_{i,j-1}+S('-', y_{j-1})\qquad(左侧的字符和空格比对)\\
\end{array}
\right.
$$
然后根据状态转移方程开始从第二行中的第二列，通过矩阵一行一行移动，计算每个位置的分数。得分被计算为从现有的分数可能的最佳得分的左侧，顶部或左上方（对角线）。当一个得分从顶部计算，或从左边这代表在我们的对准的插入缺失。当我们从对角线计算分数这表示两个字母所得位置匹配的对准。

（3）通过步骤（2）我们可以得到得分矩阵，得分矩阵的最后一个值即为我们所求答案，然后我们可以通过得分矩阵进行回溯得到对齐的两个字符串序列。

伪代码：

```
算法 LCS(A[l..m],B[l..n])
score = zeros(m+1, n+1)
for i←1 to m+1
    score[i][0] = score_matrix[A[i-1]][‘-’]
end
for j←1 to n+1
    score[0][j] = score_matrix[‘-’][B[j-1]]
end
for i←2 to m+1
for j←2 to n+1
    match = score[i-1][j-1] + score_matrix[A[i-1]][B[j-1]]
    delete = score[i-1][j] + score_matrix[A[i-1]][‘-’]
    insert = score[i][j-1] + score_matrix[‘-’][B[j-1]]

```

# 地图着色问题

该题是经典的回溯算法

算法步骤：

（1）设置最少使用颜色总数color_num，随机从color_num中随机选取一个颜色作为当前编号为node_num的省份地图颜色； 
（2）判断当前颜色是否和node_num的相邻省份重复，如果不重复就递归查询下一个城市；
（3）如果上述方案出现颜色重复现象就返回假，然后将最小使用颜色总数加1，进行下一个方案的查询知道返回为真说明当前最少使用颜色总数是我们需要的答案。

伪代码：

```
算法 Search(adjmat[l..n], node_num, colors[1..m], color_num)
if node_num >= n
    return true
else
    for i←1 to color_num
        colors[node_num] = i
        if 当前选定颜色和相邻省份不重复
            if Search(adjmat, node_num+1, colors, color_num)
                return true
            end
        end
    end
end
return false

算法 mcp(adjmat[1..n])
colors = zeros(n)
color_num←1
while true
    if Search(adjmat, 0, colors, color_num)
        break
    color_num += 1
return colors, color_num

```

