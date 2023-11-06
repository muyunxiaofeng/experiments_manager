# experiments_manager
 生物实验的管理

# 依赖包

pip install pandas

pip install numpy

pip install matplotlib

pip install scipy



# 功能汇总

1. 实现对多组数据的的离散型筛选的功能



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



# 2023.11.06

## 线性回归

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
