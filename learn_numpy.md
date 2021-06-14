# 科学计算与数据处理

## Numpy

```python
ploy1s(c_or_r,r=False,variable=None)#一维多项式类
ployval(p,x)#多项式求值，计算多项式在x处的值，p为拟合多项式系数
array([x,y,z],dtype)#
arrange()#
linspace()#
polyfit()#多项式拟合
```

## Scipy

```python
interp1d()
interp2d()
griddata()
```

## 插值问题与拟合问题

寻找近似函数 $y=f(x)$ 使函数在观测点的值等于或接近观测值。用函数 $y=f(x)$ 取代原始的函数关系 $y=g(x)$

>1)当测量数据的数据量较小并且数据值是准确的，或者基本没有误差时，一般用插值的方法。
>2) 当通过测量得到的数据比较多，或者测量值与真实值之间有一定误差时，一般用拟合的方法。

### 插值(Inrepolation)

用一个近似的函数关系式 $y=f(x)$ 来刻画一组实验观测数据中自变量$x$与因变量$y$之间的关系，要求这个近似函数曲线通过已知的所有数据点
