
from loguru import logger


# setting
# 添加一个文件输出，记录 DEBUG 及以上级别，按文件大小分割，保留最新 7 个文件
logger.add("my_app.log", level="DEBUG", rotation="1 MB", retention="7 days", compression="zip")


# session_id

# logger添加
logger.debug("这是调试信息")
logger.info("这是信息")
logger.warning("这是警告")
logger.error("这是错误")
logger.critical("这是严重错误")


# catch

@logger.catch # 装饰器用法

with logger.catch(): # 上下文管理器用法
    pass


# bind
user_logger = logger.bind(user_id="abc", session_id="xyz")
user_logger.info("User session started")
# 输出可能包含 user_id="abc", session_id="xyz"


