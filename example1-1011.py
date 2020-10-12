# -*- coding: utf-8 -*-
# DATE: Sat Oct 10 20:08:18 2020
# AUTHOR: 星级劳模李思宜
# GITHUB: KeeLee-BNU
# ************************
# 导入所需要的库
import numpy as np
import matplotlib.pyplot as plt
import math

# 数据（列表形式）
x=[0,1,2,3,4]
y=[1.1,2.2,3.3,4.4,5.5]
pi=math.pi    # 之后调用Pi就不需要写"math."
x_2 = np.arange(-pi*2, pi*2, 0.05)
y_2=2*np.sin(x_2)+2

# 设置图像,坐标轴们
fig, axs = plt.subplots(1, 2, figsize=(6, 3), sharey=True)

# 将数据用不同的图表形式表示后置于对应的轴上。
axs[0].bar(x,y)
axs[1].plot(x_2,y_2)

# 为图表添加样式
plt.yticks([-2,-1,0,1,2])
axs[1].xaxis.set_major_locator(      # 主定位器间隔，默认为1
    plt.MultipleLocator(pi)
)
axs[0].yaxis.set_major_locator(      # 主定位器间隔，默认为1
    plt.MultipleLocator(1)
)

axs[1].grid(color = 'g')
# 尝试在axs[0]中设置红色（red）的主刻度网格线


plt.show()