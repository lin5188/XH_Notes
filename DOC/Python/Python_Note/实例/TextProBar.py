'''需求分析
- 采用字符串方式打印可以动态变化的文本进度条
- 进度条需要能在一行中逐渐变化
- 采用sleep()模拟一个持续的进度
'''

#TextProBarV1.py
import time
scale = 10
print("------执行开始------")
for i in range(scale+1):
    a = '*' * i
    b = '.' * (scale - 1)
    c = (1/scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)
print("------执行结束------")

