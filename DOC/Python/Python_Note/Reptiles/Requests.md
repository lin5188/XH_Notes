Requests.md
===

安装步骤
---
1、在`开始`菜单中用管理员权限启动`cmd`命令控制台；  
2、在`cmd`中输入`pip install requests`回车；
此时，等待程序安装完成即可。

测试安装后的效果
---
启动IDLE  
1. `import Requests`  #导入Requests库
2. `r = Requests.get("http://www.baidu.com")` #以访问百度主页为例子  
3. `r.status_code` #查看状态码，返回200，表示访问成功
4. `r.encoding = 'utf-8' ` #更改字体库编码为utf-8
5. `r.text` #打印网页内容

![](DOC\Python\Python_Note\Reptiles\PNG\1.png)

Requests库的7个主要方法
---

|方法|说明|
|:---|:---|
|**requests.request()**|_构造一个请求，支撑以下各方法的基础方法_|
|__requests.get()__|_获取HTML网页的主要方法，对应于HTTP的GET_|
|**requests.head()**|_获取HTML网页头信息的方法，对应于HTTP的HEAD_|
|**requests.post()**|_向HTML网页提交POST请求的方法，对应于HTTP的POST_|
|**requests.put()**|_向HTML网页提交PUT请求的方法，对应于HTTP的PUT_|
|**requests.patch()**|_向HTML网页提交局部修改请求，对应于HTTP的PATCH_|
|**requests.delete()**|_向HTML网页提交删除请求，对应于HTTP的DELETE_|



