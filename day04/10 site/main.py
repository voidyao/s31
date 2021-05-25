
# 方式1
# import cal
#
# cal.add(2,4)
# cal.mul(3,5)

# 方式2：
# x = 10
# from cal import add
# from cal import x as x_new
#
#
# add(2,5)
# print(x)
# print(x_new)

# 导入文件：重复导入，只加载一次
# from cal import add
# from cal import sub
from logger import get_logger
import cal


if __name__ == '__main__':

	print("这是一个main文件")
	get_logger("main")
	cal.add(2, 6)

	print(__name__)  # "__mian__"




