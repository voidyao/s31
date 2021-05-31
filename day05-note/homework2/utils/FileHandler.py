

"""

关于文件处理的模块

"""

import json

from conf import settings



def read_file():
    """
    :return: 初始化，将json文件中的学生信息读出来
    """
    dic = {}
    with open(settings.INFO_FILE_PATH, 'r', encoding='utf-8') as f:
        try:
            # 如果json文件不为空
            # tmp_dic = json.load(f)
            dic.update(json.load(f))
        except Exception as e:
            # print(e)
            pass
        finally:
            return dic

def save_file(dic):
    """ 保存学生信息 """
    with open(settings.INFO_FILE_PATH, 'w', encoding='utf-8') as f:
        # tmp = json.dumps(dic)
        # f.write(tmp)
        json.dump(dic, f)
        print('数据保存成功')