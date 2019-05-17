MarkDown语法
==
该文件用于练习和展示书写README的各种markdown语法，GitHub的markdown语法在标准的基础上做了扩展，称为`GitHub Flavored MarkDown`，简称`GFM`。

***
|软件|功能
|---|---
|Python|机器语言
|SQL|数据库
***

##目录
* [横线](#横线)
* [标题](#标题)
* [文本](#文本)
    * 普通文本
    * 单行文本
    * 多行文本
    * 高亮文本
    * 换行
    * 斜体
    * 粗体
    * 删除线
* [图片](#图片)
    * 来源于网络的图片
    * GitHub仓库中的图片
* [链接](#链接)
    * 文字超链接
        *  链接外部URL
        *  链接本仓库里的URL
    *  锚点
    * [图片链接](#图片链接)
* [列表](#列表)
    * 无序列表
    * 有序列表
    * 复选框列表
* [块引用](#块引用)
* [代码高亮](#代码高亮)
* [表格](#表格)
* [表情](#表情)
* [diff语法](#diff语法)
* [数学公式语法](#数学公式语法)

 ##横线
----------------
***、---、___可以显示横线效果

***
---
___

##标题
----------------
```

#格式标题一、二级下自带下划线

直接文字下面加===为一级标题，加---为二级标题

三级以下标题需要自行添加横线

```

# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题

文本
-----

### 普通文本
--
这是普通文本

### 单行文本
---
    Hello，大家好，我是Lin。
在一行开头加入1个Tab键或4个空格。

### 多行文本（文本块）
---
#### 语法1
在连续几行的文本开头加入1个Tab或者4个空格。

    Hello，大家好
    欢迎来到Lin的学习小站
    祝您 步步高升。

#### 语法2
使用一对三反引号：
```
Hello，大家好
    欢迎来到Lin的学习小站
    您可以在知乎、CSDN、简书中搜索【维生素】找到我。
```
该语法也可实现代码高亮，见[代码高亮](#代码高亮)

### 高亮文本
---
文字高亮功能能使行内部分文字高亮，可使用一对反引号。

语法：
```
`数据分析` `Excel` `MySQL` `Python`
```
效果：`数据分析` `Excel` `MySQL` `Python`

也适合做一篇文章的tag

### 换行
---
直接回车不能换行
可以在上一行文本补两个空格，再回车
这样下一行就换行了。

或者直接在两行文本之间加一个空行。

### 斜体、粗体、删除线
---
|语法|效果
|---|---
|`*斜体1*`|*斜体1*
|`_斜体2_`|_斜体2_
|`**粗体1**`|**粗体1**
|`__粗体2__`|__粗体2__
|`***斜粗体1***`|***斜粗体1***
|`___斜粗体2___`|___斜粗体2___
|`~~删除线~~`|~~删除线~~
|`~~***斜粗体删除线1***~~`|~~***斜粗体删除线1***~~
|`***~~斜粗体删除线2~~***`|***~~斜粗体删除线2~~***

    斜体、粗体、删除线可混合使用。

### 图片
---
```
![alt](URL title)
```
alt和title即对应HTML中的alt和title属性（都可省略）：
- alt表示图片显示失败时的替换文本
- title表示鼠标悬停在图片时显示的文本（注意这里要加引号）

URL即图片的url地址，如果引用本仓库中的图片，直接使用**相对路径**就可了，如果引用其他github仓库中的图片要注意格式，即：`仓库地址/raw/分支名/图片路径`，如：
```
https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif
```
|#|语法|效果|
|---|---|----
|1|`![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")`|![baidu](http://www.baidu.com/img/bdlogo.gif "百度logo")
|2|`![][地球]`|![][地球]

注意例2的写法使用了**URL标识符**的形式，在[键接](#键接)一节有介绍。
>在文末有foryou的定义：
```
[foryou]:https://github.com/guodongxiaren/ImageCache/raw/master/Logo/foryou.gif
```

### 键接
---
#### 键接外部URL
|#|语法|效果
|---|---|---
|1|`[我的博客](https://blog.csdn.net/XH_Home/ "悬停显示")`|[我的博客](https://blog.csdn.net/XH_Home "悬停显示")
|2|`[我的知乎][zhihu]`|[我的知乎][zhihu]

语法2由两部分组成：
- 第一部分使用两个中括号，[ ]里的名称（本例中zhihu），可以是数字，字母等的组合，标识符上下对应就行了（**姑且称之为URL标识符**）
- 第二部分标记实际URL。

>使用URL名称能达到复用的目的，一般把全文所有的URL名称统一放在文章末尾，这样看起来比较干净。
>>URL名称是我起的名字，不知道是否准确。囧。。

#### 键接本仓库里的URL

|语法|效果|
|----|-----|
|`[我的简介](/example/profile.md)`|[我的简介](/example/profile.md)|
|`[example](./example)`|[example](./example)|

#### 图片键接

给图片加链接的本质是混合图片显示语法和普通的链接语法。普通的链接中[ ]内部是链接要显示的文本，而图片链接[ ]里面则是要显示的图片。
直接混合两种语法当然可以，但是十分啰嗦，为此我们可以使用URL标识符的形式。

|#|语法|效果
|---|---|---
|1|`[![weibo]()]`|



## 数学公式语法
----------------
### 方法一：使用Google Chart的服务器

```html
<img src="http://chart.googleapis.com/chart?cht=tx&chl= 在此插入Latex公式" style="border:none;">
```
    <img src="http://chart.googleapis.com/chart?cht=tx&chl= \Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" style="border:none;">
例子：
<img src="http://chart.googleapis.com/chart?cht=tx&chl= \Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}" style="border:none;">

### 方法二：使用forkosh服务器
```html
<img src="http://www.forkosh.com/mathtex.cgi? 在此处插入Latex公式">
```

例子：
<img src="http://www.forkosh.com/mathtex.cgi? \Large x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}">


### 方法三：使用MathJax引擎
Google浏览器应用商店中，搜索MathJax Plugin for Github，添加到扩展程序。
$$公式$$表示行间公式，本来Tex中使用\(公式\)表示行内公式，但因为Markdown中\是转义字符，所以在Markdown中输入行内公式使用\\(公式\\)，如下代码：
```html
<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default"></script>
```

$$x=\frac{-b\pm\sqrt{b^2-4ac}}{2a}$$
\\( x=\frac{-b\pm\sqrt{b^2-4ac}}{2a} \\)


> _**行内与独行**_

- 行内公式：将公式插入到本行内，符号：`$公式内容$`，如：$xyz$
- 独行公式：将公式插入到新的一行内，并且居中，符号：`$$公式内容$$`，如：$$xyz$$

引用自：https://www.jianshu.com/p/e74eb43960a1


[地球]：
https://github.com/lin5188/XH_Notes/blob/master/DOC/others/icons/%E6%8E%A2%E7%B4%A2%E6%98%9F%E7%90%83icon/%E6%98%9F%E6%9C%88-200.png


