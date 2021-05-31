import logging

def get_logger():
    # 返回一个日志器对象,默认WARNING级别
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        # 创建一个格式器
        fmt = logging.Formatter(
            fmt="%(asctime)s-%(name)s-%(levelname)s-%(lineno)s-%(message)s",
            datefmt="%Y/%m/%d %X"
        )
        # 创建 streamhanlder
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(logging.ERROR)

        # 创建 filehandler
        fh = logging.FileHandler(filename="test2.log", encoding="utf8")
        fh.setFormatter(fmt)

        # 为logger对象添加hander对象
        logger.addHandler(sh)
        logger.addHandler(fh)    # 创建一个格式器

    return logger

# 应用
logger1 = get_logger()
logger2 = get_logger()

logger2.debug("debug")
logger2.info("info")
logger2.warning("warning日志")
logger2.error("error")
logger2.critical("critical")


