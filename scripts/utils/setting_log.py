# -*- coding: utf_8 -*-
import logging
import logging.handlers
from datetime import datetime
import os

def set_logger(module_name):
    """ロガー設定処理
    

    Args:
        __name__: 読み込んだファイル名

    Returns:
        logger: logger
    """
    # ログ用の日時を作成
    log_date = datetime.today().strftime('%Y%m%d_%H%M%S')

    # ログ用のパスを作成
    log_abspath = os.path.abspath(os.curdir)
    logpath = os.path.join(log_abspath, "log", str(log_date) + ".log")
    
    logger = logging.getLogger(module_name)
    logger.handlers.clear()

    streamHandler = logging.StreamHandler()
    fileHandler = logging.handlers.RotatingFileHandler(logpath, maxBytes=10000, backupCount=5)

    formatter = logging.Formatter(
        "%(asctime)s [%(levelname)s] (%(filename)s | %(funcName)s | %(lineno)s) %(message)s")

    streamHandler.setFormatter(formatter)
    fileHandler.setFormatter(formatter)

    logger.setLevel(logging.DEBUG)
    streamHandler.setLevel(logging.INFO)
    fileHandler.setLevel(logging.DEBUG)

    logger.addHandler(streamHandler)
    logger.addHandler(fileHandler)
    # logger.addHandler(emailHandler)

    return logger