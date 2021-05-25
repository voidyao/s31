



print("日志的__name__：",__name__)
def get_logger(name):
    print("%s打印日志"%name)

print("这是一个日志模块")


if __name__ == '__main__':

    # 功能测试
    get_logger("xxx")