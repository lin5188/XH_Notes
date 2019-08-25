IO编程.md
===

目录：
1. 文件读写
2. 操作文件和目录
3. 序列化操作

# 1.文件读写

IO在计算机中指的是Input/Output，也就是输入输出。

在IO编程中，Stream（流）是一种重要的概念，分为输入流（Input Stream）和输出流（Output Stream）。

我们可以把流理解为一个水管，数据相当于水管中的水。

## 1.1 打开文件

Python内置了读写文件的函数，方便了文件的IO操作。

open函数用来打开文件，语法如下：

    open(name[.mode[.buffering]])

open函数使用一个文件名作为唯一的强制参数，然后返回一个文件对象。

模式（mode）和缓冲区(buffering)参数都是可选的，默认mode是读模式，默认缓冲区是无。

例：

    >>> f = open(r'c:\text\qiye.txt')

## 1.2 文件模式

open函数中的mode参数，通过改变mode参数可以实现对文件的不同操作。

|值|功能描述
|---|---
'r'|读模式
'w'|写模式
'a'|追加模式
'b'|二进制模式（可添加到其他模式中使用）
'+'|读/写模式（可添加到其他模式中使用）

>注：以二进制文件存储的mp3音乐或者图像，应该在模式参数中增加'b'，参数'rb'来读取一个二进制文件。

## 1.3 文件缓冲区

buffering参数控制着文件的缓冲。

- 参数为0，I/O操作就是'无缓冲',直接将数据写到硬盘上
- 参数为1，I/O操作就是'有缓冲'，数据先写到内存里，只有使用Flush函数或者Close函数才会将数据更新到硬盘
- 参数为>1的数字则代表‘缓冲区的大小’，单位是字节
- 参数为-1或任何负数，代表使用默认缓冲区的大小

## 1.4 文件读取
经常用到的方法有read()、readlines().

- 小文件：
    
        with open(r'e:\xml\qiye.txt','r') as f:
            print f.read()

>注：调用read()一次将文件内容读到内存，但是如果文件过大，将会出现内存不足的问题。    
- 大文件：

        with open(r'e:\xml\qiye.txt','r') as f:
            print f.read(size)
>注：一般对于大文件，可以反复调用read(size)方法，一次最多读取size个字节。           
- 文本文件：

        with open(r'e:\xml\qiye.txt\','r') as f:
            for line in f.readlines():
                print line.strip()                   

>注：对于配置文件等文本文件，使用readlines()方法更加合理。    

## 1.5 文件写入

- 方法1：

        f = open(r'e:\xml\qiye.txt','w') as f:
        f.write('qiye')
        f.close()
        
- 方法2：(推荐使用)

        with open(r'e:\xml\qiye.txt','w') as f:
            f.write('qiye')
            f.close()
            
    
# 2.操作文件和目录
在Python中对文件和目录的操作经常用到os模块和shutil模块。

下面介绍一些操作文件和目录的常用方法：

|代码|说明
|---|---
os.getcwd()|获得当前Python脚本工作的目录路径
os.listdir()|返回指定目录下的所有文件和目录。例如返回C盘下的文件：os.listdir("C:\\")
or.remove(filepath)|删除一个文件
os.removedirs(r"d:\python")|删除多个空目录
os.path.isfile(filepath)|检验给出的路径是否是一个文件
os.path.isdir(filepath)|检验给出的路径是否是一个目录
os.path.isabs()|判断是否是绝对路径
os.path.exists()|检验路径是否真的存在。例如检测D盘下是否有Python文件夹：os.path.exists(r"d:\python"）
os.path.split()|分离一个路径的目录名和文件名。例如os.path.split(r"/xml/qiye/qiye.txt"),返回结果是一个无组：（'/xml/qiye','qiye.txt'）
os.path.splitext()|分离扩展名。例如os.path.split(r"/xml/qiye/qiye.txt"),返回结果是一个无组：（'/xml/qiye/qiye','.txt'）
os.path.dirname(filepath)|获取路径名
os.path.basename(filepath)|获取文件名
os.getenv()与os.putenv()|读取和设置环境变量
os.linesep|给出当前平台使用的行终止符。Windows使用'\r\n',Linux使用'\n'而Mac使用'\r'
os.name|指示你正在使用的平台。Windows是'nt'，Linux/Unix是'posix'
os.rename(old,new)|重命名文件或者目录
os.makedirs(r"f:\惠\xml")|创建多级目录
os.mkdir("xml")|创建单个目录
os.stat(file)|获取文件属性
os.chmod(file)|修改文件权限与时间戳
os.path.getsize(filename)|获取文件大小
shutil.copytree("olddir","newdir")|复制文件夹。olddir和newdir都只能是目录，且newdir必须不存在。
shutil.copyfile("oldfile","newfile")|复制文件。oldfile和newfile都只能是文件。
shutil.copy("oldfile","newfile)|复制文件。oldfile只能是文件，newfile可以是文件，也可以是目标目录。
shutil.move("oldpos","newpos")|移动文件（目录）
os.rmdir("dir")|只能删除空目录
shutil.rmtree("dir")|删除空目录、有内容的目录



