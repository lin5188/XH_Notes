Python网络爬虫与信息提取.md
===
Requests库
---

>Requests对象的属性

|属性|说明|
|---|---
|r.status_code|HTTP请求的返回状态，200表示连接成功，404表示失败
|r.raise_for_status()|如果不是200，产生异常requests.HTTPError
|r.text|HTTP响应内容的字符串形式，即url对应的页面内容
|r.encoding|从HTTP header中猜测的响应内容编码方式
|r.apparent_encoding|从内容中分析出的响应内容编码方式（备选编码方式）
|r.content|HTTP响应内容的二进制形式

>理解Requests库的异常

|异常|说明|
|---|---
|requests.ConnectionError|网络连接错误异常，如DNS查询失败、拒绝连接等
|requests.HTTPError|HTTP错误异常
|requests.URLRequired|URL缺失异常
|requests.TooManyRedirects|超过最大重定向次数，产生重定向异常
|requests.ConnectTimeout|连接远程服务器超时异常
|requests.Timeout|请求URL超时，产生超时异常

>Requests库的7个主要方法
>>需要理解HTTP协议
- HTTP协议对资源的操作方法

|方法|说明
    |---|---
    |GET|请求获取URL位置的资源
    |HEAD|请求获取URL位置资源的响应消息报告，即获得该资源的头部信息
    |POST|请求向URL位置的资源后附加新的数据
    |PUT|请求向URL位置存储一个资源，覆盖原URL位置的资源
    |PATCH|请求局部更新URL位置的资源，即改变该处资源的部分内容
    |DELETE|请求删除URL位置存储的资源 

- 对应Requests库的方法
    
|方法|说明
|---|---
|requests.request()|构造一个请求，支撑以下各方法的基础方法
|requests.get()|获取HTML网页的主要方法，对应于HTTP的GET
|requests.head()|获取HTML网页头信息的方法，对应于HTTP的HEAD
|requests.post()|向HTML网页提交POST请求的方法，对应于HTTP的POST
|requests.put()|向HTML网页提交PUT请求的方法，对应于HTTP的PUT
|requests.patch()|向HTML网页提交局部修改请求，对应于HTTP的PATCH
|requests.delete()|向HTML页面提交删除请求，对应于HTTP的DELETE

>>HTTP协议

- URL格式 
    ```
    http://host[:prot][path]
    
    - 1. host:合法的Interest主机域名或IP地址
    - 2. port:端口号，缺少端口为80
    - 3. path:请求资源的路径
     ```
    - HTTP URL实例
        - http://www.bit.edu.cn
        - http://220.181.111.188/duty
        
    - HTTP URL的理解
        - URL是通过HTTP协议存取资源的Internet路径，一个URL对应一个数据资源。
    
>Requests库主要方法解析
## requests.request(method,url,**kwargs)
- method:请求方式，对应get/post等7种
    - 如：r = requests.request('GET',url,**kwargs)
- url:拟获取页面的url链接
- **kwargs:控制访问的参数，共13个

|参数|说明
|---|---
|1、params|字典或字节序列，作为参数增加到url中
|2、data|字典、字节序列或文件对象，作为Requests的内容
|3、json|JSON格式的数据，作为Requests的内容   
|4、headers|字典，HTTP定制头(模拟浏览器）
|5、cookies|字典或Cookiejar,Request中的cookie
|6、auth|元组类型，支持HTTP认证功能
|7、files|字典类型，传输文件
|8、timeout|设定超时时间，秒为单位
|9、proxies|字典类型，设定访问代理服务器，可以增加登录认证
|10、allow_redirects|True/False,默认为True，重定向开关
|11、stream|False,默认为True，获取内容立即下载开关
|12、verify|False,默认为True，认证SSL证书开关
|13、cert|本地SSL证书路径

例子：

    1、params
        ```python 
        >>>kv = {'key1':'value1','key2':'value2'}
        >>>r = requests,request('GET','http://python123.io/ws',params=kv)
        >>>print(r.url)
        
        执行结果：http://python123.io/ws?key1=value1&key2=value2
        ```    
    2、 data:
        ```python 
        >>> kv = {'key1':'value1','key2':'value2'}
        >>> r = requests.request('post','http://python123.io/ws',data=kv)
        >>> body = '主体内容'
        >>> r = requests.request('post','http://python123.io/ws',data=body)
        ```
    3、json:
        ```python 
        >>> kv = {'key1':'value1','key2':'value2'}
        >>> r = requests.request('post','http://python123.io/ws',json=kv) 
       ```
    4、headers:
        ```python
        >>> hd = {'user-agent':'Chrome/10'}
        >>> r = requests.request('ROST','http://python123.io/ws',headers=hd)
        >>> print(r.headers)
        ```
    5-6：下文详述
    7、files:
        ```python
        >>> fs = {'file':open('data.xls','rb')}
        >>> r = requests.request('POST','http://python123.io/ws',files=fs)
        ```
    8、timeout:略
    9、proxies:
        ```python
        >>> pxs = {'http":"http://user:pass@10.10.10.1:1234'
                   'https':'https://10.10.10.1:4321'}
        >>> r = requests.request('GET','http://www.baidu.com',proxies=pxs)
    10-13：略

## --** requests.get(url,params=None,**kwargs) **--
- url:拟获取页面的url链接
- params:url中的额外参数，字典或字节流格式，可选
- **kwargs：12个控制访问的参数

## requests.head(url,**kwargs)
- url:拟获取页面的url链接
- **kwargs：13个控制访问的参数

## requests.post(url,data=None,json=None,**kwargs)
- url:拟更新页面的url链接
- data:字典、字节序列或文件，Request的内容
- json:JSON格式的数据，Request的内容
- **kwargs：11个控制访问的参数

## requests.put(url,data=None,**kwargs)
- url:拟更新页面的url链接
- data:字典、字节序列或文件，Request的内容
- **kwargs：12个控制访问的参数

## requests.patch(url,data=None,**kwargs)
- url:拟更新页面的url链接
- data:字典、字节序列或文件，Request的内容
- **kwargs：12个控制访问的参数

## requests.delete(url,**kwargs)
- url:拟删除页面的url链接
- **kwargs：13个控制访问的参数

