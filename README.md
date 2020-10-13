# Python-_wanglab-
Resources represented during the staff meeting @2020Oct13th,BNU

文件包括：

1.PPT:Python 作图_wanglab.pdf

2.Ex1的py文件:example1.py

3.Ex1的Jupyter文件:[python_datavisualization]Ex1_Matplotlib.ipynb

3.Ex2的Jupyter文件:[python_datavisualization]Ex2_Plotly.ipynb

4.Ex2所用的数据集:py_vislz_data.csv

Tips:

1.如果想要查询某个函数中有哪些参数，可以输入下面的代码，将“go.Bar”的位置替换为所要查询的函数即可
import inspect
inspect.signature(go.Bar)

2.matplotlib显示中文标签并防止乱码的方法：
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus']=False

3.在csv文件中有一列数据：group：
data1=df.groupby('time_1').mean()['group']    # 分类索引,求每个组对应name_1的平均值，可以进一步绘制条形图进行比较
