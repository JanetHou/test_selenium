# coding: utf-8
import os

# 访问主页
home_url = "https://team.pescms.com/?g=Team&m=Login&a=index"

# 截图存放路径
screenshot_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "imgs")
# 日志存放路径
log_path = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "logs")