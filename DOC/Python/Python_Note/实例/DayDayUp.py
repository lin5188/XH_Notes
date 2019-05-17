
'''
基本问题：持续的价值
* 一年365天，每天进步1%，累计进步多少呢？  1.01的365次方
* 一年365天，每天退步1%，累计剩下多少呢？  0.99的365次方

#问题1：千分之一的力量
#DayDayUpQ1.py
dayup = pow(1.001,365)
daydown = pow(0.999,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

#运行结果：向上：1.44，向下：0.69




#问题2：千分之五或者百分之一的力量
#DayDayUpQ2.py
dayfactor = 0.005 #引入变量，修改一处就可以
dayup = pow(1+dayfactor,365)
daydown = pow(1-dayfactor,365)
print("向上:{:.2f},向下:{:.2f}".format(dayup,daydown))

#运行结果：（千分之五）
# 向上：6.17，向下：0.16

#运行结果：（百分之一）
# 向上：37.78，向下：0.03




#问题3：工作日的力量
#一年365天，一周5个工作日，每天进步百分之一
#一年365天，一周2个休息日，每天退步百分之一

#DayDayUpQ3.py
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - dayfactor)
    else:
        dayup = dayup * (1 + dayfactor)
print("工作日的力量:{:.2f}".format(dayup))

#运行结果：
#工作日的力量：4.63




#问题4：工作日的力量
#一年365天，一周5个工作日，每天进步百分之一
#一年365天，一周2个休息日，不进步也不退步

#DayDayUpQ4.py
dayup = 1.0
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup
    else:
        dayup = dayup * (1 + dayfactor)
print("工作日的力量:{:.2f}".format(dayup))

#运行结果：
#工作日的力量：13.29



#问题5：工作日模式下要努力到什么水平，才能与每天努力百分之一一样呢？

#DayDayUpQ5.py
def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.001
while dayup(dayfactor) < 37.87:
    dayfactor += 0.001
print("工作日努力的参数{:.3f}".format(dayfactor))

#运行结果
工作日努力的参数：0.019
工作日模式，每天要努力到1.9%，相当于365模式每天1%的一倍
'根据df参数计算工作日力量的函数
 参数不同，这段代码可共用
 def保留字用于定义函数
 while保留字判断条件是否成立
 条件成立时循环执行'



#练习
#DayDayUpQ5.py

def dayUp(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6,0]:
            dayup = dayup * (1 - 0.01)
        else:
            dayup = dayup * (1 + df)
    return dayup
dayfactor = 0.001
while dayUp(dayfactor) < 37.78:
    dayfactor += 0.001
print("工作日的力量是：{:.3f}".format(dayfactor))
print(pow(1.019,365))

dayup = 1
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - 0.001)
    else:
        dayup = dayup * (1 + 0.019)
print("工作日的力量：{:.3f}".format(dayup))

dayup = 1
for i in range(365):
    if i % 7 in [6,0]:
        dayup = dayup * (1 - 0.001)

    else:
        dayup = dayup * (1 + 0.011)
print("工作日的力量：{:.3f}".format(dayup))
'''

"1 + 1 = 2" + chr(10004)

