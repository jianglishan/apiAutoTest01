import logging
from logging import handlers

class InitLog():
    #设置日志格式
    fmt = "%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d - [%(message)s] "

    #创建格式器
    formatter = logging.Formatter(fmt)

    #创建控制器处理器和文件处理器
    sh = logging.StreamHandler()
    fh = logging.handlers.TimedRotatingFileHandler("./logs/log_01",when= "D",backupCount= 7,encoding="utf-8")

    #把格式器放入处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    #