# experiments_manager
 生物实验的管理

# 依赖包

pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

清华 

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

腾讯

```
pip config set global.index-url http://mirrors.cloud.tencent.com/pypi/simple
```

阿里

```
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```

临时下载

```
pip install pandas -i https://pypi.tuna.tsinghua.edu.cn/simple
```

离线安装

```
pip install xxx.whl
pyhton setup.py install
1.
也可直接使用pip

pip install xxx.tar.gz
检查

可以使用 pip list 查看第三方库是否安装完毕。
当我们拿到一个项目时，首先要在项目运行环境安装 requirement.txt 所包含的依赖：

pip install -r requirement.txt
1.
当我们要把环境中的依赖写入 requirement.txt 中时，可以借助 freeze 命令：

pip freeze >requirements.txt
```

## 目前依赖包

```shell

pip install pipreqs

pip install pandas

pip install numpy

pip install matplotlib

pip install scipy
```

pipreqs D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\support\  --encoding=utf-8 --force

# 功能汇总

## bin

1. 实现对多组数据的的离散型筛选的功能
2. digital_elisa: 
   1. 2023.11.28：
   2. 


## utils

​	1.完成字母转换为数字的方法alpha_calculator 【2023.11.11】：直接输入字符串即可，如果非英文字母，则会报错！算出来是跟excel列名一致的结果。

2023.12.06

- [x] ~~需要补充完成输入记录~~

- [x] ~~测试json模式是否生效~~

- [x] ~~增加项目选项~~

- [x] ~~增加保存布板功能~~

- [x] ~~测试布板功能~~

- [ ] ~~数据遍历、~~

- [ ] 录入项目

  - [x] 增
  - [x] 删
  - [ ] 改
  - [ ] 查

- [ ] 设计项目

  - [ ] 增
  - [ ] 删
  - [ ] 改
  - [ ] 查

- [ ] 实验记录的批量

  - [ ] 增
  - [ ] 删
  - [ ] 改
  - [ ] 查

- [ ] 数据库化

- [ ] 总分表转化

  

# 更新日志

## 2023.11.04

### 离散型数值分析

离群检验法是一种统计方法，用于确定一个数据集中的异常值。这些异常值可能由各种因素引起，例如测量错误、数据收集错误、数据传输错误等。离群检验法可以帮助我们识别和处理这些异常值，以避免其对数据分析产生负面影响。

离群检验法有多种，以下列举几种常见的：

1. 肖维勒法：根据测定次数n查肖维勒系数表值ω(n)，当ωn>ω(n)时，判定为异常值。
2. t检验法：通过计算t统计量来判断是否存在异常值。当t统计量的值大于临界值时，判定为异常值。
3. 格鲁布斯法：通过计算格鲁布斯统计量来判断是否存在异常值。当格鲁布斯统计量的值大于临界值时，判定为异常值。
4. 狄克逊法：通过计算离群值与临近值的差值与极差的比值来判断是否存在异常值。当比值大于临界值时，判定为异常值。

在应用离群检验法时，需要根据具体的数据集和分析目的选择合适的离群检验方法。同时，还需要确定适当的临界值或显著性水平，以确保检验结果的准确性和可靠性。

#### 格鲁布斯法





格鲁布斯法是一种用于判断一组数据中可疑值的取舍的方法，常用于化学数据分析。

具体步骤如下：

1. 计算出可疑数据的T值。
2. 与各显著性水平下的临界值比较。若T＞Tα(n-1)，则舍去可疑数据；若T≤Tα(n-1)，则接受可疑数据。

以上信息仅供参考，可以查阅关于格鲁布斯法的专业书籍或者咨询统计专业人士，以获取更全面和准确的信息。

###### Grubbs检验临界值表

1. 检验水准
-------

Grubbs检验是一种用于检测单个离群值的统计方法。检验水准通常设置为α，代表我们愿意接受的错误拒绝零假设的风险。典型的检验水准包括0.05和0.01。

2. 样本数量
-------

Grubbs检验需要至少两个观测值以形成一组连续的数据。因此，样本数量应大于或等于2。

3. 总体分布
-------

Grubbs检验假设数据来自正态分布。如果数据不符合正态分布，该检验可能会产生误导性的结果。

4. 检验方向
-------

Grubbs检验可以用于检测单个离群值是否存在。具体而言，我们可以测试一个假设，即数据中是否存在至少一个异常值。如果检验统计量大于临界值，则我们拒绝零假设，认为数据中存在离群值。

5. 置信水平
-------

Grubbs检验的置信水平通常与α水准相关联。例如，如果我们选择α=0.05，则置信水平为95%。这意味着，如果我们多次进行Grubbs检验，那么我们有95%的信心会得到正确的结果。

6. 临界值表
-------

临界值表是用于确定Grubbs检验结果的表格。临界值取决于检验水准、样本数量和总体标准差。在临界值表中，我们可以找到在不同样本数量和不同标准差下，对应的α水准的临界值。

7. 应用范围
-------

Grubbs检验适用于连续的数据集，其中数据之间存在时间序列关系或空间序列关系。它通常用于质量控制、金融分析、环境科学等领域，以检测异常值或离群值。在实践中，通常使用计算机软件来执行Grubbs检验，如Excel或专门的数据分析软件包。总结Grubbs检验是一种基于正态分布假设的统计方法，用于检测单变量数据集中的离群值。它具有广泛的应用范围，并且通常可以通过计算机软件轻松执行。然而，需要注意的是，如果数据不符合正态分布，该方法可能会产生误导性的结果。



格鲁布斯法是指化学中用于判断一组数据中的可疑值的取舍的方法，是检测数据中是否存在异常值的一种统计检验。这种检验通过计算样本中偏离均值最多的数据点，然后检验是否太偏离均值而说明该数据为异常值。它最早是在1950年由计算机科学家H.R.Grubbs提出的，因而得名为格鲁布斯检验。

格鲁布斯法（Grubbs法）的具体步骤如下：

1. 将测量数据按从小到大排序，设x7为可疑值。
2. 计算7个数据的平均值“X”、计算标准偏差s值。
3. 计算：疑均差=x7-“X” ；计算统计量T = 疑均差/s。
4. 判定：若T<T值，则x7保留；若T≥T值，则x7舍弃。

以上步骤仅供参考，建议查阅专业统计学书籍获取更多信息。

以下是Python实现格鲁布斯法（Grubbs法）的示例代码：


```python
import numpy as np

def grubbs_test(data):
    """
    Grubbs test for outliers detection.
    
    Parameters:
        data (list): A list of numerical data.
    
    Returns:
        list: A list of outliers. If there are no outliers, return an empty list.
    """
    # Sort the data in ascending order.
    sorted_data = sorted(data)
    n = len(sorted_data)
    
    # Calculate the mean and standard deviation.
    mean = np.mean(sorted_data)
    std = np.std(sorted_data)
    
    # Initialize the outlier list.
    outliers = []
    
    # Calculate the Grubbs test statistic for each data point.
    for i in range(1, n-1):
        x = sorted_data[i]
        mx = sorted_data[0] + (i-1)*(mean - sorted_data[0])/(n-1)
        sx = np.sqrt((n-i)*variance(sorted_data[0:i]) + (i-1)*variance(sorted_data[i:n]))
        t = abs(x - mx) / sx
        if t >= np.sqrt(2/n):
            outliers.append(x)
    
    return outliers
```
其中，`variance`函数用于计算样本方差，可以使用以下代码实现：


```python
def variance(data):
    """
    Calculate the variance of a set of data.
    
    Parameters:
        data (list): A list of numerical data.
    
    Returns:
        float: The variance of the data.
    """
    n = len(data)
    if n < 2:
        return 0.0
    mean = np.mean(data)
    deviations = [(x - mean) ** 2 for x in data]
    return np.sum(deviations) / (n - 1)
```

具体步骤如下：

1. 计算出可疑数据的T值。
2. 与各显著性水平下的临界值比较。若T＞Tα(n-1)，则舍去可疑数据；若T≤Tα(n-1)，则接受可疑数据。

以上信息仅供参考，可以查阅关于格鲁布斯法的专业书籍或者咨询统计专业人士，以获取更全面和准确的信息。

在Python中，可以使用Scipy库中的IQR函数来计算四分位数范围（IQR），并使用该函数与Zscore函数结合实现格鲁布斯法。

##### 以下是一个Python代码示例：


```python
import numpy as np
from scipy.stats import zscore

# 生成示例数据
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 计算四分位数范围（IQR）
q25, q75 = np.percentile(data, [25, 75])
iqr = q75 - q25

# 计算Z-score
z_scores = zscore(data)

# 定义格鲁布斯临界值表，可根据需要调整显著性水平
alpha = 0.05
critical_values = [1.4826, 1.7576, 2.0565, 2.3801, 2.7345, 3.1174, 3.5300, 3.9746, 4.4528, 5.0000]

# 根据Z-score判断异常值
outliers = []
for i in range(len(z_scores)):
    if abs(z_scores[i]) > critical_values[int(iqr/0.25*alpha)]:
        outliers.append(data[i])
```
在上面的示例中，首先计算了四分位数范围（IQR）和Z-score。然后根据格鲁布斯临界值表中的值，通过Z-score的绝对值与临界值的比较，判断异常值。最后将异常值存储在outliers列表中。



#### 狄克逊法

狄克逊法是一种用于检测异常值的统计方法，它是一种非参数的方法，可以有效地寻找数据集中不正常的观测值。该方法由美国统计学家布鲁斯·E·狄克逊于1950年提出，并逐渐成为检验异常值的常用方法之一。

在Python中，可以使用Scipy库中的IQR函数来计算四分位数范围（IQR），并使用该函数与Zscore函数结合实现狄克逊法。

##### 以下是一个Python代码示例：


```python
import numpy as np
from scipy.stats import zscore

# 生成示例数据
data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 计算四分位数范围（IQR）
q25, q75 = np.percentile(data, [25, 75])
iqr = q75 - q25

# 计算Z-score
z_scores = zscore(data)

# 根据Z-score判断异常值
outliers = []
for i in range(len(z_scores)):
    if abs(z_scores[i]) > iqr/0.5:
        outliers.append(data[i])
```
在上面的示例中，首先计算了四分位数范围（IQR）和Z-score。然后根据公式abs(Z-score) > IQR/0.5判断异常值，其中0.5是一个经验常数，可以根据需要调整。最后将异常值存储在outliers列表中。



在离群检验法中，T值的计算方法是根据可疑数据与相邻数据的差异，结合整个数据的标准差来计算的。具体公式如下：

T = abs(可疑数据 - 相邻数据) / 标准差

其中，相邻数据是指可疑数据前后的两个数据，标准差是整个数据集的标准差。通过计算可疑数据与相邻数据的差异，可以反映可疑数据相对于整个数据集的离散程度。然后将差异除以标准差，可以得到可疑数据的T值。

需要注意的是，在计算T值时，需要考虑整个数据集的标准差，而不是仅仅考虑相邻数据的差异。同时，T值的计算也需要结合具体的应用场景和数据分布情况来进行调整和优化。



Z-score（标准化分数）是一种基于标准化的方法，用于衡量一个特定值与数据集平均值之间的关系。具体来说，Z-score将数据集中的每个值转换为与其相对于平均值的距离成正比的标准偏差，其中标准偏差定义为每个数据点与平均值的差异。这种方法可以将不同规模或分布的数据集进行比较，并帮助识别异常值或离群点。在统计学中，Z-score也称为标准化分数，它在标准正态分布中的应用非常广泛。

Z-score的计算方法为：Z = (X - μ) / σ，其中μ是该组数据的均值，σ是该组数据的标准差，Z是标准分数。

## github中branches和tags的区别

在GitHub中，“branches”（分支）和"tags"（标签）是两个常用的概念，用于管理和组织代码库的版本控制。它们有以下区别：

Branches（分支）：

分支是代码库的并行版本，允许开发人员在不影响主要代码线的情况下进行独立的开发工作。
当创建一个分支时，它会从现有的代码库中拷贝一份副本，开发者可以在该分支上进行修改、添加和删除代码。
分支的主要用途是支持团队协作和并行开发，不同的开发人员可以在各自的分支上进行工作，并最终将它们合并到主分支上。
分支通常用于开发新功能、修复错误或实验性的修改，以便在保持主代码库稳定的同时进行开发工作。
Tags（标签）：

标签是用于标识代码库中的特定版本或里程碑的静态快照。
标签在创建后通常是不可变的，即不允许对其进行修改。它们代表了一个特定的代码状态，例如一个发布版本或一个重要的里程碑。
标签的主要用途是标记重要的版本，以便开发人员和用户可以方便地参考和访问特定版本的代码。
标签通常用于发布软件版本、标记重要的版本号或记录项目的重要状态。
联系与区别：

分支和标签都用于版本控制和管理代码库，但它们的用途和性质不同。
分支是可编辑的，允许在分支上进行开发和修改，然后将更改合并到主分支或其他分支。而标签是不可变的，代表一个特定的代码状态或版本，不允许对其进行修改。
分支用于并行开发和协作，而标签用于标记重要的版本或里程碑。
分支通常是临时的，可以在开发完成后删除或合并到其他分支。标签则是永久的，用于记录特定的代码版本。
综上所述，分支用于并行开发和临时修改，标签用于标记重要的版本或代码状态。它们在版本控制中发挥不同的作用，以支持团队协作和记录重要的里程碑。
————————————————
版权声明：本文为CSDN博主「Lntano__y」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/m0_49133355/article/details/131221005



## 2023.11.06

### 线性回归

首先，我们需要使用Python中的NumPy和matplotlib库来绘制线性回归曲线，然后使用sympy库来计算线性回归公式的系数。

以下是一个示例代码：


```python
import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve

# 定义x和y
x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 4, 5, 4, 5])

# 定义x和y的变量
x, y = symbols('x y')

# 建立线性回归方程
eq = Eq(y, 2*x + 1)

# 使用solve解方程，得到系数
coef = solve(eq, y)[0]

# 进行线性回归拟合，得到拟合曲线的数据
x_fit = np.linspace(np.min(x), np.max(x), 100)
y_fit = coef[0]*x_fit + coef[1]

# 绘制原始数据点
plt.scatter(x, y, color='blue', label='Data points')

# 绘制拟合曲线
plt.plot(x_fit, y_fit, color='red', label='Fitted line')

# 在图上添加公式
plt.text(0.5, 0.9, r'y = {:.2f}x + {:.2f}'.format(coef[0], coef[1]), ha='center', va='center', transform=plt.gca().transAxes)

# 显示图形和图例
plt.legend()
plt.show()
```
在这个示例中，我们首先定义了x和y的数据点，然后使用sympy库中的symbols函数定义了x和y的变量，并建立了线性回归方程。我们使用solve函数解方程，得到了线性回归公式的系数。接下来，我们使用NumPy库中的linspace函数生成了一组拟合曲线的数据点，并使用matplotlib库中的scatter函数绘制了原始数据点，以及使用plot函数绘制了拟合曲线。最后，我们使用text函数在图上添加了线性回归公式。



## 2023.11.07

### DataFrame是Pandas中的主要数据结构之一，本篇博客主要介绍如何DataFrame中某一列的值进行修改。

1 常规方法
  这部分主要介绍修改DataFrame列值的常规方法。为了方便后续说明先构建如下数据：

import pandas as pd
import numpy as np
df=pd.DataFrame([['A',1],['B',2],['C',5],['D',4],['E',10],['F',13],['G',8]],
                columns=['col_1','col_2'],
                index=list('abcdefg'))

```
import pandas as pd
import numpy as np
df=pd.DataFrame([['A',1],['B',2],['C',5],['D',4],['E',10],['F',13],['G',8]],
                columns=['col_1','col_2'],
                index=list('abcdefg'))

```


df结果如下：

![在这里插入图片描述](assets/d2480541e275442690659fde4f7b9cad.png)

使用常量修改DataFrame列的值
使用一个常量对DataFrame列中的数据进行修改时，代码举例如下：

```
df1=df.copy()
df1['col_1']='H'
df1.loc[['a','c','d'],'col_2']=100 #将指定索引的列值进行修改
df1.iloc[4:,-1]=200 
```


df1的结果如下：

![在这里插入图片描述](assets/5b37c71308074e6795cbbf55be86b0e6.png)


使用List\array修改DataFrame列的值
当需要对DataFrame列中的多个值进行修改时，可以使用List或array等变量型数据来对其进行修改。具体代码如下：

```
df2=df.copy()
df2['col_1']=list(range(7))
df2.loc[df2.index<='d','col_2']=np.array([15,20,25,30])
df2.iloc[4:,-1]=np.array([10,5,0])
```


df2的结果如下：

![在这里插入图片描述](assets/2fd25760e5ef4d158b7a82145487c30a.png)

使用Series/DataFrame修改DataFrame列的值
除了以上两种数据类型之外，还可以使用Series型数据来修改DataFrame列的值。但使用这种方法时，**需要索引对齐，否则会出错**。具体举例如下：

```
df3=df.copy()
df3['col_1']=pd.Series([1,2,3,4,5,6,7]) #索引不对齐时不会报错，但没有成功修改列值。
df3.loc[['a','b','c'],'col_2']=pd.Series([100,200,300],index=list('abc'))
df3.iloc[3:,-1]=pd.DataFrame([[4000],[5000],[6000],[7000]],index=list('cdef'))
```


其结果如下：

![在这里插入图片描述](assets/88886bc23336426d81f9e77af99a05f3.png)


2. replace方法
  DataFrame对象自带的方法replace()也可以实现列值的修改。该方法中的参数主要有以下几个：



| **参数**   | **作用**                                                     |
| ---------- | ------------------------------------------------------------ |
| to_replace | 确定需要修改列值的数据。可接受的数据类型有：str, regex, list, dict, Series, int, float, or None |
| value      | 指定修改后的值。可接受的数据类型有：scalar, dict, list, str, regex, default None |
| inplace    | 是否本地置换                                                 |
| limit      | 指定前后填充的最大次数                                       |
| regex      | 正则表达式符号。如果需要在to_replace中使用字符串形式的正则表达式对数据进行筛选的话，需要将其设置为True。 |
| method     | 填充方式。‘pad’, ‘ffill’, ‘bfill’, None                      |

参数	作用
to_replace	确定需要修改列值的数据。可接受的数据类型有：str, regex, list, dict, Series, int, float, or None
value	指定修改后的值。可接受的数据类型有：scalar, dict, list, str, regex, default None
inplace	是否本地置换
limit	指定前后填充的最大次数
regex	正则表达式符号。如果需要在to_replace中使用字符串形式的正则表达式对数据进行筛选的话，需要将其设置为True。
method	填充方式。‘pad’, ‘ffill’, ‘bfill’, None
————————————————
版权声明：本文为CSDN博主「Sun_Sherry」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yeshang_lady/article/details/127619031



参数	作用
to_replace	确定需要修改列值的数据。可接受的数据类型有：str, regex, list, dict, Series, int, float, or None
value	指定修改后的值。可接受的数据类型有：scalar, dict, list, str, regex, default None
inplace	是否本地置换
limit	指定前后填充的最大次数
regex	正则表达式符号。如果需要在to_replace中使用字符串形式的正则表达式对数据进行筛选的话，需要将其设置为True。
method	填充方式。‘pad’, ‘ffill’, ‘bfill’, None
创建如下数据，具体如下：

```
df=pd.DataFrame([['A','A'],['B','B'],['C',5],['D',4]],
                columns=['col_1','col_2'],
                index=list('abcd'))
```


df的结果如下：

![在这里插入图片描述](assets/a8e7f4c2a51c4c4caf21ca024caaead5.png)

对整个DataFrame中的指定数据进行替换

```
#A替换为aaa,B替换为bbb,4替换为100
df_1=df.replace(to_replace=['A','B',4],value=['aaa','bbb',100])
#将A替换为AAAA
df_2=df.replace(to_replace='A',value='AAAA')
#将A替换为AAAAA,5替换为2000
df_3=df.replace(to_replace={"A":'AAAAA',5:2000})
```


其结果如下：

![在这里插入图片描述](assets/c6fd8590162b4a769c0397e0fd18e38e.png)

对DataFrame中的不同列指定不同的替换方式

```
#对于col_1列：将A替换为1，B替换为2
#对于col_2列：将A替换为100，B替换为200
df_4=df.replace({"col_1":{'A':1,'B':2},"col_2":{"A":100,"B":200}})
```


其结果如下：

![在这里插入图片描述](assets/1a4c92861095443cbaab142b87f5d789.png)

使用正则表达式筛选数据

```
#将A\B替换成new
df_5=df.replace(to_replace=r'[AB]',value='new',regex=True)
```


其结果如下：

![在这里插入图片描述](assets/3442b68795fd4112be6b646a8f58cdfc.png)

————————————————
版权声明：本文为CSDN博主「Sun_Sherry」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/yeshang_lady/article/details/127619031

## 2023.11.09

在Python中实现离群点检测的方法有很多种，下面我简单介绍几种常见的方法：

1. **Z-Score方法**：这种方法是通过计算每个数据点与平均值的差值，再除以标准差。然后根据z-score的绝对值是否超过某个阈值来判断是否为离群点。


```python
import numpy as np

def z_score(data):
    return (data - np.mean(data)) / np.std(data)

# 假设data是我们需要检查的数据集
outliers = np.abs(z_score(data)) > 3
```
2. **IQR方法**：四分位距方法（IQR）是通过计算数据的下四分位数（Q1）和上四分位数（Q3），然后计算IQR，即Q3 - Q1。离群点被定义为小于Q1 - 1.5 * IQR或大于Q3 + 1.5 * IQR的数据点。


```python
import numpy as np

def iqr(data):
    data_sorted = np.sort(data)
    q25, q75 = np.percentile(data_sorted, 25), np.percentile(data_sorted, 75)
    iqr = q75 - q25
    lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
    return (data < upper) & (data > lower)

# 假设data是我们需要检查的数据集
outliers = iqr(data)
```
3. **基于统计的方法**：这种方法是使用一些统计测试（例如卡方检验、威尔科克森符号检验等）来检测离群点。这种方法通常需要更复杂的计算，但可以提供更准确的离群点检测。例如使用Shapiro-Wilk测试检查数据是否符合正态分布，然后使用z-score方法找出离群点。
4. **使用机器学习方法**：一些机器学习算法（例如孤立森林方法）也可以用来检测离群点。这种方法通常需要更多的计算资源，但可以更准确地找到离群点。例如使用Isolation Forest方法。

以上都是简单介绍，每种方法都有其优缺点和适用场景，需要根据具体情况选择合适的方法。



```python
class Data_washing:
    def __init__(self, data=None):
        self.origin_data = None
        self.washed_data = None
        self.washed_method = None

    def iqr(self):
        data = self.origin_data
        # 排序序列
        data_sorted = np.sort(data)
        q25, q75 = np.percentile(data_sorted, 25), np.percentile(data_sorted, 75)
        iqr = q75 - q25
        lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
        self.washed_method = inspect.currentframe().f_code.co_name
        return lower < data < upper
from i_experimnet.utils.data_wash.data_washing import Data_washing

from unittest import TestCase


class TestData_washing(TestCase):
    def test_iqr(self):
        li = [1, 2, 3, 4, 5, 6, 7, 8]
        dw = Data_washing(data=li)
        print(dw.iqr())
Ran 1 test in 0.007s

FAILED (errors=1)

Error
Traceback (most recent call last):
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\utils\data_wash\test_data_washing.py", line 27, in test_iqr
    print(dw.iqr())
          ^^^^^^^^
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\utils\data_wash\data_washing.py", line 35, in iqr
    data_sorted = np.sort(data)
                  ^^^^^^^^^^^^^
  File "C:\Users\41379\experiments_manager\Lib\site-packages\numpy\core\fromnumeric.py", line 1017, in sort
    a.sort(axis=axis, kind=kind, order=order)
numpy.exceptions.AxisError: axis -1 is out of bounds for array of dimension 0
```



从错误信息来看，问题出在`np.sort(data)`这一行代码。错误是`numpy.exceptions.AxisError: axis -1 is out of bounds for array of dimension 0`，这表明你试图在不存在的轴上对数组进行排序。

你的`iqr`方法试图对`self.origin_data`进行排序，但根据错误信息，`self.origin_data`的维度为0，也就是说它可能不是一个二维或更高维度的数组，无法进行排序。

一个可能的解决方案是确保你在调用`np.sort(data)`之前检查`data`的维度。如果`data`是一个0维数组，那么你可能需要直接返回`data`，而不是尝试对它进行排序。你可以使用以下代码：


```python
class Data_washing:
    def __init__(self, data=None):
        self.origin_data = None
        self.washed_data = None
        self.washed_method = None

    def iqr(self):
        data = self.origin_data
        if len(data.shape) == 0:  # if data is a scalar
            return data < np.percentile(data, 25) and data > np.percentile(data, 75)
        else:  # if data is an array
            data_sorted = np.sort(data)
            q25, q75 = np.percentile(data_sorted, 25), np.percentile(data_sorted, 75)
            iqr = q75 - q25
            lower, upper = q25 - 1.5 * iqr, q75 + 1.5 * iqr
            self.washed_method = inspect.currentframe().f_code.co_name
            return lower < data < upper
```
这样，当`self.origin_data`是一个标量时，它会返回一个布尔值，表示该标量是否在25%和75%的分位数之间。当`self.origin_data`是一个数组时，它将按照预期的方式进行排序并计算IQR。





### 在Python中，我们可以使用内建函数`type()`来判断一个变量的类型。例如：


```python
x = 5
print(type(x))  # 输出: <class 'int'>
```
在这个例子中，`type(x)`返回的是`<class 'int'>`，这表示`x`是一个整数类型。

### 另一个常见的内建函数是`isinstance()`，这个函数可以检查一个对象是否是一个给定的类型。例如：


```python
x = 5
print(isinstance(x, int))  # 输出: True
```
在这个例子中，`isinstance(x, int)`返回`True`，这表示`x`确实是一个整数类型。

### 在 Pandas 中，你可以通过多种方式从 DataFrame 中获取值。以下是一些基本示例：

1. **使用索引**：如果你有一个行索引，你可以直接从 DataFrame 中获取那一行的数据。例如：


```python
import pandas as pd

# 创建一个 DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['a', 'b', 'c'])

# 获取索引 'b' 的行
row = df.loc['b']
print(row)
```
这将输出：


```css
A    2
B    5
C    8
Name: b, dtype: int64
```
2. **使用列名**：如果你有一个列名，你可以直接从 DataFrame 中获取那一列的数据。例如：


```python
# 获取列 'A' 的数据
column = df['A']
print(column)
```
这将输出：


```css
a    1
b    2
c    3
Name: A, dtype: int64
```
3. **使用布尔索引**：你可以使用一个布尔数组来选择 DataFrame 中的行或列。例如：


```python
# 选择所有 'A' 值大于 1 的行
mask = df['A'] > 1
selected_rows = df[mask]
print(selected_rows)
```
这将输出：


```css
A  B  C
b  2  5  8
c  3  6  9
```
4. **使用高级索引**：你可以使用更复杂的方式选择 DataFrame 中的数据，例如使用列表、数组或字典。例如：


```python
# 选择 'A' 列中值大于 1 的行，并且 'B' 列中值小于 5 的行
mask = (df['A'] > 1) & (df['B'] < 5)
selected_rows = df[mask]
print(selected_rows)
```
这将输出：


```css
A  B  C
b  2  4  6
```

### 在Python的pandas库中，你可以使用索引来从DataFrame中取出特定的行和列。

如果你想取出某一行的数据，你可以使用`.loc`属性，它允许你通过行标签来索引行。例如：


```python
import pandas as pd

# 创建一个简单的DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['a', 'b', 'c'])

# 使用.loc取出索引为'b'的行
row = df.loc['b']
print(row)
```
这将输出：


```css
A    2
B    5
C    8
Name: b, dtype: int64
```
如果你想取出某一列的数据，你可以直接使用列的名字来索引列。例如：


```python
# 取出列'A'的数据
column = df['A']
print(column)
```
这将输出：


```css
a    1
b    2
c    3
Name: A, dtype: int64
```
如果你想取出多个行的数据，你可以提供一个包含所有行标签的列表，并用逗号分隔。例如：


```python
# 取出索引为'a'和'b'的行
rows = df.loc[['a', 'b']]
print(rows)
```
这将输出：


```css
A  B  C
a  1  4  7
b  2  5  8
```

### 在Pandas库中，你可以使用`stack()`函数将DataFrame从二维表转化为一维表。下面是一个例子：


```python
import pandas as pd

# 创建一个简单的DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}, index=['a', 'b', 'c'])

# 使用stack()函数将DataFrame转化为一维表
one_dim_df = df.stack()
print(one_dim_df)
```
这将会输出以下内容：


```python
a  A    1
   B    4
   C    7
b  A    2
   B    5
   C    8
c  A    3
   B    6
   C    9
dtype: int64
```
在这个结果中，你可以看到原来的二维表已经被转化为一维表，每个元素的索引由原来的行标签和列标签组成。

在将DataFrame转化为一维表后，你可以使用`.values`属性或者直接进行索引来取值。

如果你想获取整个一维表的值，你可以使用`.values`属性。例如：


```python
one_dim_df = df.stack()
values = one_dim_df.values
print(values)
```
这将输出一个二维的NumPy数组，其中包含了整个一维表的值。

如果你只想获取一维表中特定位置的值，你可以直接使用索引。例如：


```python
# 获取索引为(1, 'A')的元素
value = one_dim_df[1]['A']
print(value)  # 输出：2
```
### 这里，我们使用了中括号表示法来索引特定的行和列。在这个例子中，我们获取了索引为1的行中'A'列的值。如果你想将一维表转换为列表形式，并且去掉索引，你可以使用`.tolist()`方法。例如：


```python
one_dim_df = df.stack()
list_form = one_dim_df.tolist()
print(list_form)
```
这将输出一个列表，其中包含了整个一维表的值，但没有索引。每个元素都是一个包含行标签、列标签和值的元组。如果你只想获取特定位置的值，你可以直接索引列表。例如：


```python
# 获取索引为1的元素
value = list_form[1]
print(value)  # 输出：(1, 'A', 2)
```
这里，我们获取了索引为1的元素，它是一个包含行标签、列标签和值的元组。

### 如果你想将一维表转换为字典形式，你可以使用`.to_dict()`方法。

默认情况下，这将返回一个字典，其中行标签为键，列标签为值的键值对。如果你想去掉索引，你可以将`exclude`参数设置为`index`。例如：


```python
one_dim_df = df.stack()
dict_form = one_dim_df.to_dict(exclude=['index'])
print(dict_form)
```
这将输出一个字典，其中包含了行标签和列标签对应的值，但没有索引。每个键都是一个元组，包含行标签和列标签。你可以根据需要进一步处理这个字典，比如将其转换为其他数据类型。

## 2023.11.11

### 拿到一块dataframe的例子

好的，以下是一个例子，假设你有一个名为`df`的DataFrame，其中包含以下数据：


```
A B C D
a 1 2 3 4
b 5 6 7 8
c 9 10 11 12
d 13 14 15 16
```
如果你想选择第一列到第三列的数据，你可以使用`.loc`属性，如下所示：


```python
selected_data = df.loc[:, :3]
print(selected_data)
```
这将输出一个新的DataFrame，其中只包含第一列到第三列的数据：


```css
A B C
a 1 2 3
b 5 6 7
c 9 10 11
d 13 14 15
```
如果你想选择第二行到第四行、第一列到第三列的数据，你可以使用`.loc`属性，如下所示：


```python
selected_data = df.loc[2:, :3]
print(selected_data)
```
这将输出一个新的DataFrame，其中包含了第二行到第四行、第一列到第三列的数据：


```css
A B C
c 9 10 11
d 13 14 15
```

### 完成字母转换为数字的方法alpha_calculator

## 2023.11.13

### 在Python的pandas库中，我们可以通过定位特定的行和列然后赋值来改变DataFrame中的特定区域的值。以下是一个示例：


```python
import pandas as pd

# 创建一个简单的DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

print("原始DataFrame:")
print(df)

# 将区域[0, 'A': 'B']的值设为0
df.iloc[0, df.columns['A':'B']] = 0

print("\n赋值后的DataFrame:")
print(df)
```
在这个例子中，我们选择了第一行（索引为0），并且选择了列'A'到'B'（这是通过列的名字和它们之间的冒号表示的）。然后，我们将这个区域的所有值设为了0。

注意，`df.columns['A':'B']`返回的是列'A'到'B'的索引，这样我们就可以在`iloc`中使用它来定位我们想要修改的列。

如果你想要修改的区域跨越了多个行或列，你可以通过增加`iloc`的参数来定位你想要修改的行和列。例如，如果你想要修改第1行到第2行（索引为0和1），以及列'A'到'B'（包括列'A'和'B'），你可以这样做：


```python
df.iloc[0:2, df.columns['A':'B']] = 0
```
这样，所有在指定行和列范围内的数据都将被设置为0。

## 2023.11.14

### 在Python的pandas库中，你可以很容易地将DataFrame转化为列表。这可以通过使用`.values.tolist()`方法实现。下面是一个例子：


```python
import pandas as pd

# 创建一个DataFrame
df = pd.DataFrame({
   'A': [1, 2, 3],
   'B': [4, 5, 6],
   'C': [7, 8, 9]
})

# 将DataFrame转化为列表
df_list = df.values.tolist()

print(df_list)
```
运行以上代码，会输出以下结果：


```python
[    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9]
]
```
### 这就是将DataFrame的每一行转化为一个列表的方法。如果你想将整个DataFrame转化为一个单一的列表，可以按列进行操作，如下所示：


```python
flat_list = df.values.flatten().tolist()
print(flat_list)
```
这将输出：


```python
[1, 4, 7, 2, 5, 8, 3, 6, 9]
```

## 思路更新-2023.11.14：

从每次单独的设置一个plate进行跨分  方便拓展

```py
            return

    def area_split(self, area):
        if "-" in area:
            position_start, position_end = area.split("-")
            print(position_start)
            # 获取字母部分
            position_start_alpha = re.findall(self._config.re_alpha, position_start.upper())[0].strip()
            # 获取数字部分
            position_start_digit = re.findall(self._config.re_digit, position_start)[0].strip()
            # 获取字母部分
            position_end_alpha = re.findall(self._config.re_alpha, position_end.upper())[0].strip()
            # 获取数字部分
            position_end_digit = re.findall(self._config.re_digit, position_end)[0].strip()
            return {
                self._config.position_start_alpha: position_start_alpha,
                self._config.position_start_digit: int(position_start_digit),
                self._config.position_end_alpha: position_end_alpha,
                self._config.position_end_digit: int(position_end_digit)
            }
        else:
            # 获取字母部分
            position_alpha = re.findall(self._config.re_alpha, area.upper())[0].strip()
            # 获取数字部分
            position_digit = re.findall(self._config.re_digit, area.upper())[0].strip()
            return {
                self._config.position_alpha: position_alpha,
                self._config.position_digit: int(position_digit)
            }

    def set_value_position(self, sub_area, area_value):
        """
        多个范围对应一个值
        :param sub_area:
        :param area_value:
        :return:
        """
        self.modify_plate = self.values_plate.copy()
        # 分割区域
        area_dict = self.area_split(sub_area)
        if len(area_dict) == 2:
            # 单点赋值
            # 呈现结果赋值
            self.values_plate.loc[
                area_dict[self._config.position_alpha], area_dict[self._config.position_digit]] = area_value
            # 获取位置信息
            # todo 将参数字典抽出来放在 config 中
            coordinates = self.position_plate.loc[
                area_dict[self._config.position_alpha], area_dict[self._config.position_digit]]
            params_dict = {
                self._config.params_position: coordinates,
                self._config.params_value: area_value
            }
            self.change_modify_plate(row=area_dict[self._config.position_alpha],
                                     col=area_dict[self._config.position_digit],
                                     params_dict=params_dict)
        else:

            # 先要判定大小
            if self._config.position_start_digit > self._config.position_end_digit:
                # 如果是反的 则调换位置
                self._config.position_start_digit, self._config.position_end_digit = \
                    self._config.position_end_digit, self._config.position_start_digit

            # 赋值
            self.values_plate.loc[
            area_dict[self._config.position_start_alpha],
            area_dict[self._config.position_start_digit]:area_dict[self._config.position_end_digit]] = area_value
            # 构造参数字典的参数字典
            kw = {
                self._config.params_position: self.param_position,
                self._config.params_value: self.param_value
            }
            self.batch_change_modify_plate(
                row_start=area_dict[self._config.position_start_alpha],
                row_end=area_dict[self._config.position_end_alpha],
                col_start=area_dict[self._config.position_start_digit],
                col_end=area_dict[self._config.position_end_digit],
                para=area_value,
                **kw
            )

    def set_area_to_many_values(self, sub_area, area_values, parameter):
        """
        根据输入的参数输入参数可以将参数修改
        :param sub_area:
        :param area_values:
        :param parameter:
        :return:
        """
        self.modify_plate = self.values_plate.copy()
        # 分割区域
        area_dict = self.area_split(sub_area)
        value_dict = self.area_split(area_values)

        # 先要判定大小
        if self._config.position_start_digit > self._config.position_end_digit:
            # 如果是反的 则调换位置
            self._config.position_start_digit, self._config.position_end_digit = \
                self._config.position_end_digit, self._config.position_start_digit
        # 让前缀相等
        if value_dict[self._config.position_start_alpha] != value_dict[self._config.position_end_alpha]:
            value_dict[self._config.position_end_alpha] = value_dict[self._config.position_start_alpha]
        # 生成名称列表
        if value_dict[self._config.position_start_digit] < value_dict[self._config.position_end_digit]:
            param_values_list = [f"{value_dict[self._config.position_start_alpha]} - {num}" for num in
                                 range(self._config.position_start_digit, self._config.position_end_digit + 1)]
        else:
            param_values_list = [f"{value_dict[self._config.position_start_alpha]} - {num}" for num in
                                 range(self._config.position_start_digit, self._config.position_end_digit + 1, -1)]
        # 将字母转化为数字
        row_start = alpha_calculator.alpha_calculator(area_dict[self._config.position_start_alpha])
        row_end = alpha_calculator.alpha_calculator(area_dict[self._config.position_end_alpha])
        col_start = area_dict[self._config.position_start_digit]
        col_end = area_dict[self._config.position_end_digit]
        # 比较大小反向则倒置
        if row_start > row_end:
            row_start, row_end = row_end, row_start
        if col_start > col_end:
            col_start, col_end = col_end, col_start
        index = 0
        for _col in range(col_start, col_end + 1):
            for _row in range(row_start, row_end + 1):
                self._row = _row
                self._col = _col
                # 构造参数字典的参数字典
                para_dict = {
                    parameter: self.param_value
                }
                self.batch_change_modify_plate(
                    row_start=_row,
                    row_end=_row,
                    col_start=_col,
                    col_end=_col,
                    para=param_values_list[index],
                    parameter=self.param_value
                    # **para_dict
                )

    def change_modify_plate(self, row, col, params_dict: dict, **kwargs):
        # 构建 json,
        # 获取 modify 的值
        mj = self.modify_plate.loc[row, col]
        # 无论是不是空值都扔进去
        jb = Json_Bean(mj)
        # 赋值位置信息和值
        for param in params_dict:
            jb.input_para(var_name=param, var_value=params_dict[param])

        # 将处理后的值赋回去
        self.modify_plate.loc[row, col] = jb.json_bean()

    def batch_change_modify_plate(self, row_start, row_end, col_start, col_end, para, **kwargs):
        # 将字母转化为数字
        row_start = alpha_calculator.alpha_calculator(row_start)
        row_end = alpha_calculator.alpha_calculator(row_end)
        # 比较大小反向则倒置
        if row_start > row_end:
            row_start, row_end = row_end, row_start
        if col_start > col_end:
            col_start, col_end = col_end, col_start
        # 根据模板获取要分析的区域
        to_handle_area = self.position_plate.iloc[row_start - 1:row_end, col_start - 1:col_end]
        # 将分析的区域并扁平化转化为列表
        to_handle_area_list = to_handle_area.values.flatten().tolist()
        exit()

        for _col in range(col_start, col_end + 1):
            for _row in range(row_start, row_end + 1):
                self._row = plate_number.upper_row(_row)
                self._col = _col
                self.parameter = para
                print(self._row, self._col)
                params_dict = dict()
                print(kwargs)
                for kwarg in kwargs:
                    # {kwarg => self._config.params_position
                    # kwargs[kwarg] => self.param_position >>>()
                    params_dict[kwarg] = kwargs[kwarg]()

                # 逐个修改参数
                self.change_modify_plate(
                    row=self._row, col=self._col,
                    params_dict=params_dict
                )

    """
    参数方法的分界线
    
    """

    def param_position(self):
        """
        返回这个点的坐标值
        :return:
        """
        return self.position_plate.loc[self._row, self._col]

    def param_value(self):
        """
        返回这个点的值
        :return:
        """
        return self.parameter

```

在Python中，有一些特殊的魔法函数可以用来打印类和对象的信息。这些函数通常以`__`（双下划线）开头和结尾，这种命名方式是为了防止与实例方法或变量名冲突。

以下是一些常用的魔法函数：

1. `__str__(self)`：这个函数返回一个对象的字符串表示形式，当使用`print()`函数打印对象时，会调用这个函数。
2. `__repr__(self)`：这个函数返回一个对象的官方字符串表示形式，通常比`__str__(self)`更详细。在Python解释器中直接输入对象名称时，会调用这个函数。
3. `__len__(self)`：这个函数返回对象的长度（例如，对于列表或字符串），当使用`len()`函数时，会调用这个函数。
4. `__eq__(self, other)`：这个函数检查两个对象是否相等，当使用`==`操作符时，会调用这个函数。
5. `__ne__(self, other)`：这个函数检查两个对象是否不相等，当使用`!=`操作符时，会调用这个函数。
6. `__lt__(self, other)`：这个函数检查一个对象是否小于另一个对象，当使用`<`操作符时，会调用这个函数。
7. `__le__(self, other)`：这个函数检查一个对象是否小于或等于另一个对象，当使用`<=`操作符时，会调用这个函数。
8. `__gt__(self, other)`：这个函数检查一个对象是否大于另一个对象，当使用`>`操作符时，会调用这个函数。
9. `__ge__(self, other)`：这个函数检查一个对象是否大于或等于另一个对象，当使用`>=`操作符时，会调用这个函数。

这些魔法方法可以帮助你更好地控制你的对象的行为，并在必要时提供更多的信息。

## 2023.11.15

### dir（）/vars()

使用`dir()`函数获取的变量可能不完全准确的原因是，`dir()`函数返回的是对象的所有属性，包括它的方法和嵌套的属性。因此，如果你只对类中的实例变量感兴趣，那么需要进一步筛选和处理`dir()`函数返回的结果。

在上面的示例代码中，我们使用`isinstance()`函数和`getattr()`函数来筛选出字符串类型的属性，从而得到类中的实例变量。但是，这并不是一种完全准确的方法，因为有些变量可能是其他类型的对象，只是这些对象的行为类似于字符串。此外，如果类中有同名的方法或嵌套的属性，那么使用`dir()`函数获取的变量可能会包含这些方法或嵌套的属性。

因此，如果你需要获取类中准确的实例变量，可以考虑使用Python内置的`vars()`函数。`vars()`函数返回对象的所有实例变量，不包括它的方法和嵌套的属性。例如：


```python
class MyClass:
    def __init__(self):
        self.attribute1 = "Hello"
        self.attribute2 = 123
        self.attribute3 = "World"
    
    def method1(self):
        pass

obj = MyClass()
vars = vars(obj)
print(vars)  # {'attribute1': 'Hello', 'attribute2': 123, 'attribute3': 'World'}
```
在上面的代码中，`vars()`函数返回了对象`obj`的所有实例变量，不包括它的方法。这样可以得到更准确的类中实例变量的列表。

### 在Python的pandas库中，你可以使用`concat()`函数或者`merge()`函数来横向或竖向合并两个DataFrame。

1. 横向合并 (按行): 使用`concat()`函数


```python
import pandas as pd

# 创建两个DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                   'B': ['B0', 'B1', 'B2'],
                   'C': ['C0', 'C1', 'C2'],
                   'D': ['D0', 'D1', 'D2']},
                  index=[0, 1, 2])

df2 = pd.DataFrame({'A': ['A3', 'A4', 'A5'],
                   'B': ['B3', 'B4', 'B5'],
                   'C': ['C3', 'C4', 'C5'],
                   'D': ['D3', 'D4', 'D5']},
                  index=[3, 4, 5])

# 横向合并
result = pd.concat([df1, df2])
```
2. 竖向合并 (按列): 使用`concat()`函数，设置`axis=1`


```python
import pandas as pd

# 创建两个DataFrame
df1 = pd.DataFrame({'A': ['A0', 'A1'],
                   'B': ['B0', 'B1']},
                  index=[0, 1])

df2 = pd.DataFrame({'C': ['C0', 'C1'],
                   'D': ['D0', 'D1']},
                  index=[0, 1])

# 竖向合并
result = pd.concat([df1, df2], axis=1)
```
3. 基于列的合并: 使用`merge()`函数


```python
import pandas as pd

# 创建两个DataFrame
df1 = pd.DataFrame({'key': ['K0', 'K1'],
                   'value': ['V0', 'V1']})

df2 = pd.DataFrame({'key': ['K0', 'K1'],
                   'other_value': ['OV0', 'OV1']})

# 基于列的合并
result = pd.merge(df1, df2, on='key')
```
这些函数默认在合并时不会改变数据的顺序，但你可以使用`sort=True`参数来改变合并后的顺序。同时，请注意，这些操作默认不会改变原始DataFrame，如果你想改变原始DataFrame，你可以设置`inplace=True`。



### 在Pandas DataFrame中，你可以使用`.loc`或`.iloc`方法来按列取出DataFrame中的一块区域的值。

`.loc`方法是基于列标签的数据选择方法，你可以通过指定列标签来取出指定列的数据。例如，如果你有一个DataFrame，其中包含列"A"、"B"和"C"，你可以使用以下代码按列取出"A"列的数据：


```python
import pandas as pd

# 创建一个示例DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# 使用.loc方法取出"A"列的数据
a_column = df.loc[:, 'A']
print(a_column)
```
这将输出以下内容：


```python
0    1
1    2
2    3
3    4
Name: A, dtype: int64
```
如果你想要按行索引取出指定行的数据，可以使用`.iloc`方法。例如，如果你想要取出第1行和第3行的数据，可以像下面这样使用`.iloc`方法：


```python
import pandas as pd

# 创建一个示例DataFrame
data = {'A': [1, 2, 3, 4],
        'B': [5, 6, 7, 8],
        'C': [9, 10, 11, 12]}
df = pd.DataFrame(data)

# 使用.iloc方法取出第1行和第3行的数据
selected_rows = df.iloc[[0, 2]]
print(selected_rows)
```
这将输出以下内容：


```python
   A  B  C
0  1  5  9
2  3  7  11
```

### 要将Pandas DataFrame存储到MySQL数据库中，你可以使用Python的mysql-connector库。下面是一个基本的步骤：

1. 首先，确保你已经安装了mysql-connector。如果没有，可以通过pip进行安装：


```
pip install mysql-connector-python
```
2. 导入必要的库：


```python
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
```
3. 创建一个MySQL连接：


```python
# 填写你的数据库信息
mydb = mysql.connector.connect(
  host="localhost", # your host, usually localhost
  user="yourusername", # your username
  password="yourpassword", # your password
  database="mydatabase" # name of the data base
)
```
4. 创建一个SQL引擎，这个引擎将用于执行所有的SQL查询：


```python
engine = create_engine('mysql+mysqlconnector://{user}:{pw}@localhost/{db}'.format(user=mydb.user, pw=mydb.password, db=mydb.database))
```
5. 使用Pandas的to_sql方法将DataFrame存储到MySQL：


```python
# 假设你的DataFrame名为df
df.to_sql('my_table', con = engine, if_exists = 'replace', index=False)
```
在这个例子中，'my_table'是你要存储的表的名称。'if_exists'参数决定当表已经存在时如何处理。'replace'意味着如果表已经存在，那么将其替换。你也可以选择'append'（将新数据添加到现有表中）或'fail'（如果表存在，则不进行任何操作）。最后，`index=False`表示我们不想将DataFrame的索引存储为数据库中的列。

### 要将Pandas DataFrame存储到Excel文件中，你可以使用Pandas库的`to_excel`方法。下面是一个基本的步骤：

首先，确保你已经安装了openpyxl库，这是一个用于读写Excel文件的库。如果没有安装，可以通过pip进行安装：


```
pip install openpyxl
```
然后，你可以使用以下代码将DataFrame存储到Excel文件中：


```python
import pandas as pd

# 创建一个示例DataFrame
data = {'Name': ['John', 'Emma', 'Tom'], 'Age': [25, 30, 35], 'City': ['New York', 'Paris', 'London']}
df = pd.DataFrame(data)

# 将DataFrame存储到Excel文件中
df.to_excel('output.xlsx', index=False)
```
在这个例子中，`output.xlsx`是你想要创建的Excel文件的名称。`index=False`表示我们不想将DataFrame的索引存储到Excel文件中。如果你想要将索引存储到Excel文件中，可以省略这个参数或将其设置为`True`。

### 导出项目的依赖包有多种方式，具体方式如下：

1. 你可以通过pip list命令导出项目所需的所有依赖包。首先，在Anaconda PowerShell Prompt中执行“pip list --format=freeze”命令，然后将输出的依赖包信息重定向到一个文本文件中。
2. 如果只需要导出当前项目所需的依赖包，可以进入项目目录，然后执行“pip freeze > requirements.txt”命令。这将导出当前环境中的所有包及其路径，并将其保存到requirements.txt文件中。
3. 如果你使用的是pipreqs插件，可以按照以下步骤导出项目的依赖包：首先，安装pipreqs插件；然后，切换到项目的根目录；最后，执行“pipreqs ./”命令即可导出项目所调用的包。

需要注意的是，如果你使用的是多虚拟环境，需要进入到指定的虚拟环境中执行安装和导出命令。另外，不同的操作系统和终端环境可能存在差异，具体操作可能会有所不同。

### 在PyCharm中导出虚拟环境中的依赖包，可以按照以下步骤进行操作：

1. 打开PyCharm，并打开你的项目。
2. 确保你已经在PyCharm中配置了正确的虚拟环境。你可以通过选择"File"（文件）菜单中的"Settings"（设置）选项，然后选择"Project: [your_project_name]"（项目：[你的项目名称]）下的"Project Interpreter"（项目解释器）来配置虚拟环境。
3. 在PyCharm的底部状态栏中，找到并点击"Terminal"（终端）按钮。这将打开一个终端窗口，你可以在其中执行命令。
4. 在终端窗口中，使用以下命令导出虚拟环境中的依赖包：


```
pip freeze > requirements.txt
```
这个命令会将当前虚拟环境中的所有包及其版本信息导出到名为"requirements.txt"的文件中。
5. 等待命令执行完成，然后就会在当前目录下生成一个名为"requirements.txt"的文件，其中包含了虚拟环境中的所有依赖包信息。

现在你可以使用这个"requirements.txt"文件来重新创建相同的虚拟环境，或者将其提供给其他人使用。



### 你遇到的问题是尝试更改 PowerShell 的执行策略时被拒绝，这通常是由于权限问题导致的。在尝试执行 `Set-ExecutionPolicy` 命令时，你可能没有足够的权限来更改执行策略。

无法加载文件 C:\Users\41379\experiments_manager\Scripts\activate.ps1。未对文件 C:\Users\41379\experiments_manager\Scripts\activate.ps1 进行数字签名。无法在当前系统上运行该脚本。有关运行脚本和设置执行策略的详细信息，请参阅 https:/go .microsoft.com/fwlink/?LinkID=135170 中的 about_Execution_Policies。    + CategoryInfo          : SecurityError: (:) []，ParentContainsErrorRecordException    + FullyQualifiedErrorId : UnauthorizedAccess


要解决这个问题，你有几个选项：

1. **以管理员身份运行 PowerShell**：你可以尝试以管理员身份运行 PowerShell，这可以通过在 PowerShell 的快捷方式上右键点击并选择“以管理员身份运行”来实现。
2. **使用管理员权限运行 PowerShell 命令**：如果你已经在 PowerShell 中，你可以尝试使用 `runas` 命令来以管理员权限运行 PowerShell。在命令提示符中输入 `runas /user:Administrator "powershell.exe"`，然后按 Enter。这会尝试以管理员权限运行 PowerShell。如果系统要求你输入管理员密码，请输入密码并按 Enter。
3. **更改执行策略的当前用户的权限**：你可以运行以下命令来更改当前用户的执行策略：


```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted -Force
```
这会更改当前用户的执行策略，而不需要管理员权限。请注意，这将仅对当前用户有效，而不会影响其他用户。

如果你已经以管理员身份运行 PowerShell，但仍然遇到这个问题，那可能是因为你的账户没有足够的权限来更改执行策略。在这种情况下，你可能需要联系你的系统管理员以获取必要的权限。





### 导出python当前项目依赖清单requirements.txt

[![二愣子](assets/v2-daf47703e5469fd7acbce2084828efe7_l.jpg)](https://www.zhihu.com/people/mambazyd-5)

[二愣子](https://www.zhihu.com/people/mambazyd-5)

[](https://www.zhihu.com/question/48510028)

高等教育行业 教师

关注他

**平时我们在编写或者使用别人的Python项目时，往往会看到一个文档requirements.txt，该文档是描述一个Python项目中依赖的第三方库的名称以及版本。本文介绍只导出python当前项目依赖包操作步骤。**

#### 方法一：

如果每个项目有对应的虚拟虚拟环境，那么使用pycharm的终端里，在当前项目下，直接实现使用命令：pip freeze > requirements.txt #pip命令生成依赖性清单

#### 方法二：

注意：如果在python项目全局环境里直接使用 pip freeze > requirements.txt 会导出大量与该项目无关的依赖，包括很多个包信息，其实这里是把你当前 python 环境的所有包的相关信息导出来了。如果我们只需导出当前项目所需的依赖包，还可以采用另外一种方式，使用工具：pipreqs

##### 步骤一、安装pipreqs：

```text
pip install pipreqs
```

![img](assets/v2-3bf3567cd63f0485a87bc33c2133cea0_720w.png)

##### 步骤二：进入当前项目目录下，导出依赖清单

```text
pipreqs ./
```

![img](assets/v2-4aad15e939809919a5d2ce263e282f86_720w.png)

如果遇到编码错误UnicodeDecodeError，则将指定编码为utf8：

```text
pipreqs ./ --encoding=utf8
pipreqs ./ --encoding='iso-8859-1' 
```

(导包完成会在项目路径下生成一个requirements.txt文件)

![img](assets/v2-d6bd9c99a6ca5bcbf9f740e1975d0fdc_720w.png)

![img](assets/v2-6e33a40d811aab093e1cbd038ac72855_720w.png)

#### 方法三：使用pycharm 的工具导出requirements.txt

在pycharm上，找到Tool工具，选择Sync Python Requirements，如下：

![img](assets/v2-29c32f723d194f295e139be1722db1f4_720w.png)

![img](assets/v2-8f6a5e558107f3b43930fd6474e5c537_720w.png)

在项目根目录下就会生成requirements.txt文档

![img](assets/v2-bb40e70bb7d4e926ea3f84a1db2286c5_720w.png)



后续安装该项目的依赖时，即可直接使用：

pip install -r requirements.txt

养成良好的编程习惯。



## 2023.11.17

### 除了`all()`函数，Python还提供了其他一些内置函数，如`any()`函数，它用于检查给定可迭代对象中的是否有至少一个元素为True。

### 要从Excel加载数据到pandas（pd）中，你可以使用pandas的`read_excel()`函数。以下是一个基本的示例：


```python
import pandas as pd

# 读取Excel文件
data = pd.read_excel('your_file.xlsx')

# 显示数据的前几行
print(data.head())
```
在这个例子中，`'your_file.xlsx'`应替换为你的Excel文件的实际路径和文件名。该函数将返回一个pandas DataFrame，你可以使用这个DataFrame进行数据分析。

如果你的Excel文件中有多个工作表，并且你希望指定一个特定的工作表，你可以这样做：


```python
data = pd.read_excel('your_file.xlsx', sheet_name='your_sheet_name')
```
在这里，`'your_sheet_name'`应替换为你想要加载的工作表的名称。





### `drop_duplicates()` 是 pandas 库中的一个函数，用于在 DataFrame 中删除重复的行。以下是使用 `drop_duplicates()` 函数的一些示例：

1. 删除所有重复行：


```python
import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

df = df.drop_duplicates()
```
2. 根据某一列或几列删除重复行：


```python
import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8]}
df = pd.DataFrame(data)

df = df.drop_duplicates(subset=['A'])  # 根据列 'A' 删除重复行
```
3. 根据多个列删除重复行：


```python
import pandas as pd

data = {'A': [1, 2, 3, 4], 'B': [5, 6, 7, 8], 'C': [1, 2, 3, 4]}
df = pd.DataFrame(data)

df = df.drop_duplicates(subset=['A', 'B'])  # 根据列 'A' 和 'B' 删除重复行
```
4. 指定保留重复行的规则：


```python
import pandas as pd

data = {'A': [1, 2, 2, 3], 'B': [5, 6, 6, 7]}
df = pd.DataFrame(data)

df = df.drop_duplicates(keep='first')  # 保留第一个出现的重复行，删除后续出现的重复行
```

### 要创建一个名为items和path的空DataFrame，您可以使用以下代码：


```python
import pandas as pd

# 创建一个空的DataFrame
df = pd.DataFrame(columns=['items', 'path'])

print(df)
```
在这个例子中，我们使用pandas的DataFrame函数创建一个空的DataFrame，并指定列名为'items'和'path'。结果将是一个没有任何行数据的空DataFrame。

### 在Python的pandas库中，你可以使用`append()`函数将数据添加到DataFrame的末尾。以下是一个简单的示例：


```python
import pandas as pd

# 创建一个DataFrame
df = pd.DataFrame({
   'A': ['A0', 'A1', 'A2', 'A3'],
   'B': ['B0', 'B1', 'B2', 'B3'],
   'C': ['C0', 'C1', 'C2', 'C3'],
   'D': ['D0', 'D1', 'D2', 'D3']},
   index=[0, 1, 2, 3])

# 创建一个新的行数据
new_data = pd.Series(['A4', 'B4', 'C4', 'D4'], index=['A', 'B', 'C', 'D'])

# 使用append()函数将新数据添加到DataFrame的末尾
df = df.append(new_data)

print(df)
```
在这个例子中，我们首先创建了一个DataFrame `df`，然后创建了一个新的行数据 `new_data`。我们使用`append()`函数将 `new_data` 添加到 `df` 的末尾。最后，我们打印出更新后的 `df`。



### `append()` 函数的返回值是包含新添加的行数据的整个新 DataFrame。这意味着，当你使用 `append()` 函数将一行数据添加到 DataFrame 时，该函数将返回一个包含新添加的数据和原有数据的完整 DataFrame。你可以将这个返回值存储在一个变量中，以便后续使用。

以下是一个简单的示例：


```python
import pandas as pd

# 创建一个空的 DataFrame
df = pd.DataFrame(columns=['items', 'path'])

# 添加一行数据到 DataFrame
new_row = {'items': 'item1', 'path': 'path1'}
new_df = df.append(new_row, ignore_index=True)

print(new_df)
```
在这个例子中，我们首先创建了一个空的 DataFrame `df`。然后，我们使用 `append()` 函数将一个包含新数据的行添加到 DataFrame 中，并将结果存储在变量 `new_df` 中。最后，我们打印出新的 DataFrame `new_df`，它包含新添加的行数据。



如果你想在原始DataFrame中进行修改，而不是创建一个新的DataFrame，你可以使用`loc`或`iloc`方法来添加新行。

使用`loc`方法，你可以通过行标签来添加新行。下面是一个示例：


```python
import pandas as pd

# 创建一个包含两行数据的 DataFrame
df = pd.DataFrame({'items': ['item1', 'item2'], 'path': ['path1', 'path2']})

# 添加一行数据到 DataFrame
new_row = pd.Series(['item3', 'path3'], index=['items', 'path'])
df = df.loc[df.index.max() + 1] = new_row

print(df)
```
在这个例子中，我们首先创建了一个包含两行数据的DataFrame `df`。然后，我们使用`loc`方法通过行标签来添加新行。我们使用`df.index.max()`来获取最后一行的索引，然后将其加1作为新行的索引，并将新行数据赋值给该索引。最后，我们打印出新的DataFrame `df`，它包含新添加的行数据。

另一种方法是使用`iloc`方法通过整数位置来添加新行。以下是一个示例：


```python
import pandas as pd

# 创建一个包含两行数据的 DataFrame
df = pd.DataFrame({'items': ['item1', 'item2'], 'path': ['path1', 'path2']})

# 添加一行数据到 DataFrame
new_row = pd.Series(['item3', 'path3'])
df = df.iloc[2] = new_row

print(df)
```
在这个例子中，我们首先创建了一个包含两行数据的DataFrame `df`。然后，我们使用`iloc`方法通过整数位置来添加新行。我们使用`df.shape[0]`来获取DataFrame的行数，并将其加1作为新行的位置，并将新行数据赋值给该位置。最后，我们打印出新的DataFrame `df`，它包含新添加的行数据。

## 2023.11.18

这个错误是因为你可能正在使用一个较旧版本的Pandas库，该版本中`DataFrame`对象没有一个`append`方法。这是一个常见的错误，特别是在使用旧版本的Python或Pandas时。

如果你正在使用的是Pandas 1.2.0或更高版本，那么这个错误不应该出现，因为`DataFrame`对象应该具有`append`方法。

### 解决方案是确保你正在使用较新版本的Pandas库。你可以通过以下步骤来升级Pandas库：

1. 打开命令行或终端。
2. 输入以下命令来卸载当前版本的Pandas库：
```arduino
pip uninstall pandas
```
3. 输入以下命令来安装最新版本的Pandas库：
```bash
pip install pandas --upgrade
```
4. 重新运行你的代码。

如果你不确定你正在使用哪个版本的Pandas库，可以尝试在命令行或终端中输入以下命令来查看已安装的Pandas版本：


```css
pip show pandas
```
确保你安装的是最新版本，然后重新运行你的代码，看看问题是否得到解决。





### 这个错误信息来自Pandas库，表明你正在试图用一组标量值（即单一的数字或字符串，而不是数组或列表）创建一个`DataFrame`，但没有提供一个索引。

在你的代码中，`self.params_df = pd.DataFrame(kwargs, columns=list(kwargs.keys()))`这一行正在尝试创建一个`DataFrame`。`kwargs`是一个字典，它的键是参数名，值是参数值。看起来像这样：


```python
kwargs = {'protocol': '0.5 μg/mL'}
```
当你尝试使用这个字典创建一个`DataFrame`时，Pandas试图将字典的值转换为数据框的行。但是，字典的值是标量值（在这种情况下是一个字符串），而不是数组或列表。因此，Pandas需要一个索引来对应这些标量值。如果没有提供索引，就会出现这个错误。

解决这个问题的一种方法是将标量值转换为列表。这样就可以创建一个数据框，其中每一行都是字典的一个条目。你可以通过以下方式将字典的值转换为列表：


```python
kwargs_list = [list(v) for v in kwargs.values()]
```
然后，你可以使用这个列表和字典的键来创建`DataFrame`：


```python
self.params_df = pd.DataFrame(kwargs_list, columns=list(kwargs.keys()))
```
这样，你的代码就会像这样：


```python
kwargs = {'protocol': '0.5 μg/mL'}
kwargs_list = [list(v) for v in kwargs.values()]
self.params_df = pd.DataFrame(kwargs_list, columns=list(kwargs.keys()))
```
这应该能解决你的问题。

## 2023.11.21

### 在 Pandas 中，你可以通过使用列的名字或者列的索引来获取 DataFrame 中的某一列。

1. 使用列的名字:


```python
df['column_name']
```
在这里，`df` 是你的 DataFrame，而 `'column_name'` 是你想要获取的列的名字。

2. 使用列的索引：


```python
df.columns[index]
```
在这里，`df` 是你的 DataFrame，而 `index` 是你想要获取的列的索引。请注意，索引是从 0 开始的。所以，如果你想要获取第一列，你应该使用 `df.columns[0]`。

下面是一个完整的例子：


```python
import pandas as pd

# 创建一个 DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40]}
df = pd.DataFrame(data)

# 获取 'Name' 列
names = df['Name']
print(names)
```
这将输出：


```bash
0    Alice
1      Bob
2    Charlie
3     David
Name: Name, dtype: object
```

## 2023.11.22

### 在Python中，字典对象的`update()`方法用于合并字典。它接受一个字典或者任何可迭代的键值对序列，然后将这些键值对添加到当前字典中。如果键已经存在于字典中，那么对应的值将被更新为提供的值。

以下是`update()`方法的一些示例：


```python
# 创建一个字典
dict1 = {"a": 1, "b": 2, "c": 3}

# 使用另一个字典更新
dict2 = {"a": 4, "b": 5, "d": 6}
dict1.update(dict2)
print(dict1)  # 输出: {'a': 4, 'b': 5, 'c': 3, 'd': 6}

# 使用键值对序列更新
dict1.update([("c", 7), ("e", 8)])
print(dict1)  # 输出: {'a': 4, 'b': 5, 'c': 7, 'd': 6, 'e': 8}
```
在上述例子中，如果键已经存在于字典中，那么对应的值将被更新为提供的值。如果键不存在于字典中，那么新的键值对将被添加到字典中。

注意，`update()`方法接受两个参数，第一个参数是用于更新的字典或可迭代对象，第二个参数是可选的，它指定用于更新的字典或可迭代对象中的某个特定元素。但是在Python的更新版本中，这个特性可能已经不再适用。因此，在实际使用中需要注意更新的语法和Python版本。

## 2023.11.28

- [x] 需要补充完成输入记录
- [x] 测试json模式是否生效
- [x] 增加项目选项
- [x] 增加保存布板功能
- [x] 测试布板功能
- [ ] 

```
Launching unittests with arguments python -m unittest test_digital_elisa.TestDigital_Elisa in D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\bin


==================== finally ====================
     1     2     3     4     5     6     7     8     9     10    11    12
A  None  None  None  None  None  None  None  None  None  None  None  None
B  None  None  None  None  None  None  None  None  None  None  None  None
C  None  None  None  None  None  None  None  None  None  None  None  None
D  None  None  None  None  None  None  None  None  None  None  None  None
E  None  None  None  None  None  None  None  None  None  None  None  None
F  None  None  None  None  None  None  None  None  None  None  None  None
G  None  None  None  None  None  None  None  None  None  None  None  None
H  None  None  None  None  None  None  None  None  None  None  None  None
Plate class
例： a1-a3,a4,a5=0;b12=1000;(fg/mL); ^curve:a1-h6;^sample:a7-h7,a7-h12;{进入分散样本命名方法}; [sample_name<sample_number~6>sample_type%sample_from]sample_direction:h1-h7;
请输入位置信息，用区域间用分号隔开，只输入Q退出：选择参数
0    digital_elisa_protocol
1                     beads
Name: items, dtype: object
请输入要选择的序号，只输入Q退出，输入N新建：beads


Ran 1 test in 4.756s

FAILED (errors=1)

Error
Traceback (most recent call last):
  File "C:\Users\41379\experiments_manager\Lib\site-packages\pandas\core\indexes\base.py", line 3790, in get_loc
    return self._engine.get_loc(casted_key)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "index.pyx", line 152, in pandas._libs.index.IndexEngine.get_loc
  File "index.pyx", line 181, in pandas._libs.index.IndexEngine.get_loc
  File "pandas\_libs\hashtable_class_helper.pxi", line 2606, in pandas._libs.hashtable.Int64HashTable.get_item
  File "pandas\_libs\hashtable_class_helper.pxi", line 2630, in pandas._libs.hashtable.Int64HashTable.get_item
KeyError: 0

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\bin\test_digital_elisa.py", line 32, in test_guidance
    d = digital_elisa.Digital_Elisa()
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\bin\digital_elisa.py", line 34, in __init__
    self.guidance()
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\bin\digital_elisa.py", line 48, in guidance
    select_par = self.select_params()
                 ^^^^^^^^^^^^^^^^^^^^
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\bin\digital_elisa.py", line 122, in select_params
    param_dataframe = self.saving_list.params_select(select_item)
                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\OneDrive\201.python\pythonWorkSpace\experiments_manager\i_experimnet\middleware\writing_or_loading_info_from_excel.py", line 162, in params_select
    path = row_number.loc[0, "path"]
           ~~~~~~~~~~~~~~^^^^^^^^^^^
  File "C:\Users\41379\experiments_manager\Lib\site-packages\pandas\core\indexing.py", line 1146, in __getitem__
    return self.obj._get_value(*key, takeable=self._takeable)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\41379\experiments_manager\Lib\site-packages\pandas\core\frame.py", line 4012, in _get_value
    row = self.index.get_loc(index)
          ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\41379\experiments_manager\Lib\site-packages\pandas\core\indexes\base.py", line 3797, in get_loc
    raise KeyError(key) from err
KeyError: 0

```

### 如果你想在构建DataFrame时，列名为10个，但值只有6个，想要用`None`补齐其他的值，可以使用`pandas`库来实现。下面是一个示例代码：


```python
import pandas as pd

# 假设你有10个列名，但只有6个值
columns = ['col1', 'col2', 'col3', 'col4', 'col5', 'col6', 'col7', 'col8', 'col9', 'col10']
values = ['value1', 'value2', 'value3', 'value4', 'value5', 'value6']

# 创建一个空的DataFrame
df = pd.DataFrame(columns=columns)

# 填充值，将其他位置用None补齐
for i, value in enumerate(values):
    df.at[i, 'col'+str(i+1)] = value
    for j in range(len(columns) - len(values)):
        df.at[i+j+1, columns[i+j+1]] = None

print(df)
```
这段代码首先创建了一个空的DataFrame，然后使用循环逐个填充值，将其他位置用`None`补齐。在循环中，通过`at`方法访问DataFrame的特定位置并赋值。请注意，这里假设列名和值的顺序是对应的。如果实际情况不同，你需要相应地调整代码。



## 2023.12.06

在读取Excel文件时，如果遇到科学计数法表示的数字，可以使用`pd.read_excel`函数的`float_precision`参数来指定浮点数的精度。

默认情况下，Pandas会将科学计数法表示的数字转换为浮点数，但有时由于Excel单元格的格式问题或其他原因，可能会导致数字的精度丢失或改变。在这种情况下，您可以使用`float_precision`参数来指定浮点数的精度。

以下是一个示例代码，演示如何使用`float_precision`参数来读取Excel文件中的科学计数法表示的数字：


```python
import pandas as pd

# 读取Excel文件
df = pd.read_excel('data.xlsx', float_precision='high')

# 打印前5行数据
print(df.head())
```
在上面的代码中，`float_precision='high'`指定了高精度的浮点数表示方式，这可以避免精度丢失或改变的问题。您可以根据需要选择不同的精度表示方式，例如`float_precision='round_trip'`表示使用默认的精度设置。

### 2024年01月18日

```
Python使用不同的库来创建Excel文件

Python Developer

于 2023-03-23 11:45:53 发布

阅读量301
 收藏 1

点赞数
文章标签： python excel pandas
版权
Python使用不同的库来创建Excel文件
openpyxl:
pandas:
xlwt:

在Python中，可以使用不同的库来创建Excel文件。以下是其中几个流行的库和使用它们创建Excel文件的代码示例：
openpyxl:
import openpyxl
# 创建工作簿
workbook = openpyxl.Workbook()

# 创建工作表
worksheet = workbook.active

# 写入数据
worksheet['A1'] = 'Hello'
worksheet['B1'] = 'World'

# 保存工作簿
workbook.save('example.xlsx')
1
2
3
4
5
6
7
8
9
10
11
12
13
pandas:
import pandas as pd

# 创建数据
data = {'Name': ['John', 'Jane', 'Bob', 'Mary'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Paris', 'London', 'Tokyo']}

# 创建DataFrame
df = pd.DataFrame(data)

# 保存DataFrame到Excel文件
df.to_excel('example.xlsx', index=False)
1
2
3
4
5
6
7
8
9
10
11
12
当使用 pandas 创建 Excel 文件时，可以使用许多选项来自定义输出，包括指定工作表的名称，数据类型，数字格式等等。以下是使用 pandas 创建 Excel 文件的更详细示例：

import pandas as pd

# 创建数据
data = {'Name': ['John', 'Jane', 'Bob', 'Mary'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Paris', 'London', 'Tokyo']}

# 创建DataFrame
df = pd.DataFrame(data)

# 创建Excel文件对象
writer = pd.ExcelWriter('example.xlsx', engine='xlsxwriter')

# 将DataFrame写入工作表
df.to_excel(writer, sheet_name='Sheet1', index=False)

# 获取工作表对象
worksheet = writer.sheets['Sheet1']

# 设置单元格格式
cell_format = writer.book.add_format({'num_format': '$#,##0.00'})
worksheet.set_column('C:C', None, cell_format)

# 保存工作簿
writer.save()

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
在这个示例中，使用 pd.ExcelWriter 创建了一个 ExcelWriter 对象，它使用了 xlsxwriter 引擎。接下来，使用 to_excel() 方法将 DataFrame 写入名为 Sheet1 的工作表中，并使用 index=False 参数指定不写入行索引。然后，使用 writer.sheets 获取工作表对象并使用 set_column() 方法设置单元格格式，最后使用 writer.save() 保存工作簿。

除了上面示例中的示例之外，pandas 还提供了其他选项，例如：

sheet_name 参数可以用来指定工作表的名称。
startrow 和 startcol 参数可以用来指定写入数据的起始行和起始列。
header 参数可以用来指定是否在工作表中写入列标题。
float_format 参数可以用来指定浮点数格式。
更多示例和选项，请查看 pandas 文档。

xlwt:
import xlwt

# 创建工作簿
workbook = xlwt.Workbook()

# 创建工作表
worksheet = workbook.add_sheet('Sheet1')

# 写入数据
worksheet.write(0, 0, 'Hello')
worksheet.write(0, 1, 'World')

# 保存工作簿
workbook.save('example.xls')
1
2
3
4
5
6
7
8
9
10
11
12
13
14
这只是几个例子，Python中还有其他库可以用来创建Excel文件
————————————————
版权声明：本文为CSDN博主「Python Developer」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/qzw985/article/details/129727332
```

### 软件开发的多层模型是一种将应用程序划分为多个层次的架构模式，每个层次都有明确的职责和功能。这种模式可以用于构造可以分解为子任务组的程序，每个子任务都处于一个特定的抽象级别，每个层都为下一个层提供更高层次的服务。

在多层模型中，常见的有四层模型，包括表示层、应用层、业务逻辑层和数据访问层。每一层都有其特定的职责，例如表示层负责用户交互，业务逻辑层处理业务处理，数据访问层负责数据存储等。这种分层架构有助于提高软件的可维护性、可扩展性和安全性。

除了多层模型，还有一些其他的架构模式，如客户端-服务器模式、主从设备模式等。这些模式在特定的应用场景中各有优势，可以根据项目的需求选择合适的架构模式。

此外，还有一些软件开发的流程模型，如瀑布模型、迭代增量模型和敏捷开发模型等。这些模型在软件开发过程中各有优缺点，可以根据项目的特点和需求选择合适的流程模型。

以上信息仅供参考，如需了解更多信息，建议查阅软件工程相关书籍或咨询专业人士。

### 好的，以下是这些模型的具体实现方式和优缺点：

1. 瀑布模型：

实现方式：瀑布模型是一种线性的软件开发模型，将软件开发过程划分为一系列阶段，每个阶段都有明确的输入和输出。

优点：瀑布模型为整个项目提供了清晰的检查点，有利于大型软件开发人员的组织管理及工具的使用与研究，可以提高开发的效率。

缺点：瀑布模型是严格按照线性方式进行的，无法适应用户需求变更，用户只能等到最后才能看到开发成果，增加了开发风险。如果开发人员与客户对需求理解有偏差，到最后开发完成后，最终成果与客户需求可能会差之千里。

2. 分层模型：

实现方式：分层模型将应用程序划分为多个层次，每个层次都有明确的职责和功能。这种模式可以用于构造可以分解为子任务组的程序，每个子任务都处于一个特定的抽象级别，每个层都为下一个层提供更高层次的服务。

优点：各层之间相互独立，降低层与层之间的依赖，有利于标准化；可以降低开发风险；开发人员可以只关注整个结构中的其中某一层；可以很容易的用新的实现来替换原有层次的实现；有利于各层逻辑的复用。

缺点：降低了系统的性能；有时会导致级联的修改。

3. 原型模型：

实现方式：原型模型是在需求分析阶段制作原型，与用户沟通，及时在设计阶段避免需求偏差。

优点：克服瀑布模型的缺点，减少由于软件需求不明确带来的开发风险。

缺点：所选用的开发技术和工具不一定符合主流的发展；快速建立起来的系统结构加上连续的修改可能会导致产品质量低下。

4. 螺旋模型：

实现方式：螺旋模型分为四个阶段即制定计划、风险分析、实施工程以及客户评估。以原型为基础，加上瀑布模型重复沿着以上几个步骤进行开发。

优点：设计上的灵活性,可以在项目的各个阶段进行变更；以小的分段来构建大型系统,使成本计算变得简单容易；客户认可这种公司内部的开发方式带来的良好的沟通和高质量的产品；降低了失败和更改需求的风险。

缺点：需要大量的时间和资源投入；需要强大的管理能力和技术能力。

以上信息仅供参考，如需了解更多信息，建议查阅软件工程相关书籍或咨询专业人士。



### 在Python的pandas库中，你可以使用`drop`函数来删除DataFrame中的某一行。以下是一个简单的示例：


```python
import pandas as pd

# 创建一个简单的DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 40],
        'City': ['New York', 'Paris', 'London', 'Tokyo']}
df = pd.DataFrame(data)

# 打印原始DataFrame
print("原始DataFrame:")
print(df)

# 删除索引为1的行（即'Bob'这一行）
df = df.drop(1)

# 打印删除行后的DataFrame
print("\n删除行后的DataFrame:")
print(df)
```
在这个例子中，我们首先创建了一个包含姓名、年龄和城市的简单DataFrame。然后，我们使用`drop`函数删除了索引为1的行（即'Bob'这一行）。请注意，DataFrame的索引是从0开始的，所以索引1实际上是第二行。

### 要从DataFrame中删除某列为特定值的行，你可以使用布尔索引。假设你想删除'Name'列中值为'Bob'的行，你可以这样做：


```python
df = df[df['Name'] != 'Bob']
```
这里，`df['Name'] != 'Bob'`会返回一个布尔序列，其中为True的位置表示'Name'列中的值不是'Bob'。然后，这个布尔序列被用来从原始DataFrame中选择行。

