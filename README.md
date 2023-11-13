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

## utils

​	1.完成字母转换为数字的方法alpha_calculator 【2023.11.11】：直接输入字符串即可，如果非英文字母，则会报错！算出来是跟excel列名一致的结果。

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
