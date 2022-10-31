import logging
import os
from testdata import common_data as c_data


# 日志操作类
class LogOperation():
    logger_ = logging.getLogger("logger")

    @classmethod
    def init_logger(cls):
        # 设置过handler的证明已经初始化过了
        if not LogOperation.logger_.handlers:
            LogOperation.logger_.setLevel(logging.DEBUG)
            if not os.path.exists(c_data.log_path):
                os.mkdir(c_data.log_path)
            all_log_name = os.path.join(c_data.log_path, "all.log")
            error_log_name = os.path.join(c_data.log_path, "error.log")
            # 创建日志文件handler
            all_hl = logging.FileHandler(all_log_name, 'a', "utf-8")
            err_hl = logging.FileHandler(error_log_name, 'a', 'utf-8')
            all_hl.setLevel(logging.DEBUG)
            err_hl.setLevel(logging.ERROR)
            # 创建控制台handler
            stream_hl = logging.StreamHandler()
            stream_hl.setLevel(logging.INFO)

            # 定义日志输出的格式
            formatter = logging.Formatter('%(asctime)s - %(filename)s - '
                                          '%(levelname)s - %(message)s')
            all_hl.setFormatter(formatter)
            err_hl.setFormatter(formatter)
            stream_hl.setFormatter(formatter)

            # logger绑定handler
            LogOperation.logger_.addHandler(all_hl)
            LogOperation.logger_.addHandler(err_hl)
            LogOperation.logger_.addHandler(stream_hl)

            all_hl.close()
            err_hl.close()
            stream_hl.close()

    @staticmethod
    def get_logger():
        LogOperation.init_logger()
        return LogOperation.logger_


# print("log success")
logger = LogOperation().get_logger()




