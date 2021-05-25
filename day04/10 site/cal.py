# from logger import get_logger
import logger
print("cal的__name__：",__name__)

def add(x,y):
	logger.get_logger("add")
	print(x+y)

def mul(x,y):
	print(x*y)

def sub(x,y):
	print(x-y)

x = 100

print("这是一个计算模块")