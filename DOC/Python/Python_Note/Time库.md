Time库.md
===

Time库是Python中处理时间的标准库

Time库包括三类函数
---
- 时间获取：  
    `time()`、`ctime()`、`gmtime()`  
- 时间格式化：  
    `strftime()`、`strptime()`
- 程序计时：  
    `sleep()`、`perf_counter()`  

### **时间获取**
1. time():获取当前时间戳，即计算机内部时间值，返回`浮点数`     
`>>>time.time()   
155824094.9919252

2. ctime():获取当前时间并以易读方式表示，返回`字符串`    
`>>>time.ctime()  
'Sun May 19 14:08:48 2019'

3. gmtime():获取当前时间，表示为计算机可处理的时间格式  
`>>>time.gmtime()  
time.struct_time(tm_year=2019,tm_mon=5,tm_mday=19,tm_hour=6,tm_min=27,tm_sec=20,tm_wday=6,tm_yday=139,tm_isdst=0)

### **时间格式化**  
将时间以合理的方式展示出来  
- 格式化：类似字符串格式化，需要有展示模板
- 展示模板由特定的格式化控制符组成
- strftime()方法  

|函数|描述|
|:---:|:---
|strftime(tpl,ts)|tpl是格式化模板字符串，用来定义输出效果\n ts是计算机内部时间类型变量\n >>>t = time.gmtime() \n >>>time.strftime("%Y-%m-%d %H:%M:%S",t) \n '2019-5-21 13:17:53'
 |strptme(str,tpl)| 
- 控制符

|格式化字符串|日期/时间说明|值范围和实例
|:---:|:---:|:---
%Y|年份|0000-9999,例如：1900
%m|月份|01-12,例如：10
%B|月份名称|January-December，例如：April
%b|月份名称缩写|Jan-Dec,例如：Apr
%d|日期|01-31，例如：25
%A|星期|Monday-Sunday，例如：Wednesday
%a|星期|Mon-Sun，例如：Wed
%H|小时（24h制）|00-23，例如：12
%I|小时（12h制）|01-12，例如：7
%p|上/下午|AM,PM，例如：PM
%M|分钟|00-59，例如：26
%S|秒|00-59，例如：26






