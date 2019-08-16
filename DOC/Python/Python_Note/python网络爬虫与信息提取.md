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
|requests.requests()|构造一个请求，支撑以下各方法的基础方法
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

    
    
       

