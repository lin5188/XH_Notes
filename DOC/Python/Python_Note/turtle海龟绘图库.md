Turtle库.md
==

Python蟒蛇实例
--

```python
import turtle 
turtle.setup(650,350,200,200)
turtle.penup()
turtle.fd(-250)
turtle.pendown()
turtle.pensize(25)
turtle.pencolor("purple")
turtle.seth(-40)
for i in range(4):
    turtle.circle(40,80)
    turtle.circle(-40,80)
turtle.circle(40,80/2)
turtle.fd(40)
turtle.circle(16,180)
turtle.fd(40 * 2/3)
turtle.done()
```
    
### 举一反三
- Pythony语法元素理解  
    - Python蟒蛇绘制共17行代码，但很多行类似
    - 清楚理解这17行代码能够掌握Python基本绘图方法
    - 参考框架结构、逐行分析、逐词理解
    
- 程序参数的改变
    - Python蟒蛇的颜色：黑色、白色、七彩色……
    - Python蟒蛇的长度：1节、3节、10节……
    - Python蟒蛇的方向：向左走、斜着走……
    
- 计算问题的扩展
    - Python蟒蛇绘制问题是各类图像绘制问题的代表
    - 圆形绘制、五角星绘制、国旗绘制、机器猫绘制……
    - 掌握绘制一条线的方法，就可以绘制整个世界
    
### Python蟒蛇绘制思考
> 问题1  计算机绘图是什么原理？

- 一段程序为何能够产生窗体？为何能在窗体上绘制图形？

> 问题2   Python蟒蛇绘制从哪里开始呢？


- 如何绘制一条线？如何绘制一个弧形？如何绘制一条蟒蛇？

turtle库的使用
==
- turtle库基本介绍
- turtle绘图窗体布局
- turtle空间坐标体系
- turtle角度坐标体系
- RGB色彩体系

turtle库基本介绍
--


turtle绘图窗体布局
--
![](1)
![](2)
需要设置窗体大小或位置值才用setup,一般时候可省略

turtle空间坐标体系
--
- 绝对坐标  
![](3)  
```
turtle.goto(x,y)  
让在任何位置的海龟，到指定的坐标位置
```
![](4)

- 海龟坐标  
![](5)  
![](6)

```python
turtle.fd(d) #向海龟的正前方向运行
turtle.bk(d) #向海龟的反方向运行
turtle.circle(r,angle)  #以海龟当前位置左侧的某一个点为圆心，进行曲线运行
```

turtle角度坐标体系
--
- 绝对角度  
![](7)

```python
turtle.seth(angle)
# 用seth来改变当前海龟的角度，angle为绝对度数
```
![](8)  

- 海龟角度  
![](9)  
```python
turtle.left(angle) 
turtle.right(angle)
#分别让海龟向左或者向右改变运行方向
```
> 例：绘制“Z”型曲线   
```python
import turtle
turtle.left(0)
turtle.fd(150)
turtle.right(135)
turtle.fd(300)
turtle.left(135)
turtle.fd(150)
turtle.done()
```
RGB色彩体系
--
- 常用RGB色彩  
![](10)
![](10-1)

- 色彩模式切换  
turtley库默认使用小数值，可切换为整数值
```python
turtle.colormode(mode)
- 1.0:RGB小数值模式
- 255：RGB整数值模式
```

turtle程序语法元素分析
==
- 库引用与import
- turtle画笔控制函数
- turtle运动控制函数
- turtle方向控制函数
- 基本循环语句
- “Python蟒蛇绘制”代码分析

### ![](A1)库引用与import
___

- 使用import保留字完成，采用<a>.<b>()编码风格
    
    
    import <库名>
    <库名>.<函数名>(<函数参数>)






[A1]:
https://github.com/lin5188/XH_Notes/blob/master/DOC/others/icons/%E6%B0%B4%E6%9E%9Cicon/%E8%A5%BF%E7%93%9C-16.png
