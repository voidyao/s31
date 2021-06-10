import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
# ------------ 关于db的配置 --------

INFO_FILE_NAME = 'info.json'
INFO_FILE_PATH = os.path.join(BASE_DIR, 'db', INFO_FILE_NAME)
print(INFO_FILE_PATH)




