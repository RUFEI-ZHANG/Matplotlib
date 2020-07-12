#!/usr/bin/env python
# coding: utf-8

# ## Matplotlib绘图模板

# In[56]:


import matplotlib.pyplot as plt
import random
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False
plt.figure(dpi=100)
plt.subplot(2,1,1)
x=range(50)
y=[random.uniform(10,16) for i in x]
plt.xlabel("x轴")
plt.ylabel("y轴")
#绘制折线图
plt.plot(x,y,color="b",linestyle="-.",label="曲线一")
#显示图例
plt.legend()
#自定义刻度标签
x_label=["数字{}".format(i) for i in x]
plt.xticks(x[::5],x_label[::5])
plt.yticks(range(0,20,2))
#显示网格
plt.grid(linestyle="--",alpha=0.5)
plt.subplot(2,2,3)
#绘制散点图
plt.scatter(x,y,color="r",linestyle="--")
plt.subplot(2,2,4)

tt=["标签一","标签二","标签三"]
x_bar=[1,2,3]
y_bar=[5,2,7]
y_bar1=[4,6,3]
ticks=range(len(x_bar))
plt.bar(x_bar,y_bar,color=["r"],width=0.3)
plt.bar([i+0.3 for i in x_bar],y_bar1,color=["b"],width=0.3)
plt.xticks([i+0.15 for i in x_bar],tt,fontsize=5)

#调整子图间距
plt.subplots_adjust(left=None, bottom=None, right=None, top=None,
                wspace=0.3, hspace=0.5)
plt.show()

