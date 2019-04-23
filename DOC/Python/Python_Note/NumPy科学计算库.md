NumPy.md
===
NumPy是一个开源的Python科学计算基础库。
- 一个强大的N维数组对象ndarray  
- 广播功能函数  
- 整合C/C++/Fortran代码的工具
- 线性代数、傅里叶变换、随机数生成等功能  
`NumPy是SciPy、Pandas等数据处理或科学计算库的基础。`


> 数据维度的Python表示

- 一维数据：列表和集合类型
    [3.1398,3.1349,3.1376] 有序
    {3.1398,3.1349,3.1376} 无序
- 二维数据：列表类型
- 多维数据：列表类型  
    [ 
    [3.1398,3.1349,3.1376],[3.1413,3.1404,3.1401] 
    ]
- 高维数据：字典类型或数据表示格式（JSON、XML和YAML格式）  
    dict = {  
            "firstName" : "Li",  
            "lastName"  : "XuHui",  
            }

> NumPy的引用  

    import NumPy as np
  
N维数组对象：ndarray
---
ndarray是一个多维数组对象，由两部分构成：
- 实际的数据
- 描述这些数据的元数据（数据维度、数据类型等）

`ndarray数组一般要求所有元素类型相同，数组下标从0开始。`


例：计算A平方+B立方，其中，A和B是一维数组  

- 普通写法
```python
def pySum():  
     a = [0,1,2,3,4]  
     b = [9,8,7,6,5]  
     c = []
        
     for i in range(len(a))：
         c.append(a[i]**2 + b[i]**3)
        
     return c
     
print(pySum())
```
- **ndarray写法**
```python
import numpy as np
def npSum():
    a = np.array([0,1,2,3,4])
    b = np.array([9,8,7,6,5])
    
    c = a**2 +b**3
    
    return c
    
print(npSum())
```
### ndarray实例

![1](DOC/Python/Python_Note/图片/1.png)

|代码|代码说明|
|:---:|:---
|np.array()|生成一个ndarray数组，ndarray在程序中的别名是：array

> ndarray对象的属性

 ![2](DOC/Python/Python_Note/图片/2.png)

实例：

![3](DOC/Python/Python_Note/图片/3.png)

 
 
 
  
