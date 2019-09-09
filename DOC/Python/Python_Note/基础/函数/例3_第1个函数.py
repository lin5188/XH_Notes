'''
def say_hello():
    """打招呼"""

    print("hello 1")
    print("hello 2")
    print("hello 3")

#只有在程序中，主动调用函数，才会让函数执行
say_hello()

print("Nice！")
'''



def my_sum(L):
	"""累加平方和

	:param L:计算的最大值
	:return:累加L以下的平方之和
	"""
	sum = 0
	for x in L:
		sum = sum + x * x
		return sum


my_sum([1,2,3,4,5])