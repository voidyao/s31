import logging

LOG_FORMAT = "%(asctime)s-%(name)s-%(levelname)s-%(lineno)s-%(message)s "#配置输出日志格式
DATE_FORMAT = '%Y/%m/%d  %H:%M ' #配置输出时间的格式，注意月份和天数不要搞乱了

logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                    filename=r"test.log", #有了filename参数就不会直接输出显示到控制台，而是直接写入文件
                    filemode = "w"
                    )

logging.debug("debug日志")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")



