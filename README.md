<script type="text/javascript"
 src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
 </script>
> 前言

从这篇文章起，我将开一个坑来记录我学习Machine Learning的历程。

本文参考自Andrew NG教授的Machine Learning公开课，*[这里](http://openclassroom.stanford.edu/MainFolder/DocumentPage.php?course=MachineLearning&doc=exercises/ex2/ex2.html)*是题目链接

>题目分析

题目给出了50个数据样本点，数据的特征只有一个，就是小朋友的年龄Y是小朋友对应的身高。数据点绘制如下：

![points](http://image-kelegai.qiniudn.com/points.png)

通过上面的散点图可以看出这是个典型的线性回归题目，所采用的线性回归模型是

$$
h_\theta(x) =\theta^Tx= \sum_{i=0}^n\theta_ix_i
$$

采用梯度下降法对$\theta$进行更新，

$$
\theta_j:=\theta_j-\alpha\frac{1}{m}\sum_{i=1}^m(h_\theta(x^{(i)}-y^{(i)})x_j^{(i)}
$$

题目已经给出了$\alpha=0.07$。这里需要注意的是，由于对$\theta_j$更新时用到了$\theta$，所以一定要在所有$\theta_j$都计算结束后再对$\theta$更新。

题目已给出循环次数为1500次。

>实验结果

我给$\theta$赋初值均为1，经过1500次迭代之后，$\theta$收敛的最后结果是：

$$
\theta_0=0.7502, 
\theta_1=0.0639
$$

绘图如下：

![points](http://image-kelegai.qiniudn.com/bestFit.png)

绘图结果符合预期。

>实验代码

实验的代码用python2.7编写，用到了numpy进行数据处理，matplotlib进行绘图。
