#!/bin/bash
# -*- coding: utf-8 -*-


"""

及格率：(低于及格线个数÷总成绩个数)×100%
平均值：全部成绩的总合÷总成绩个数
方差：所有成绩的平方和 ÷ 总成绩个数 - 平均值的平方

(语文成绩的平方 + 数学成绩的平方 + 英语成绩的平方) / 3 - (((语文成绩 + 数学成绩 + 英语成绩) / 3) ** 2)

1. 添加学生信息   学生姓名 学号 语文成绩 数学成绩 英语成绩
2. 根据学生学号查看学生成绩
3. 统计：各学生的 平均成绩
4. 根据学号修改学生信息
5. 根据学号删除学生
6. 保存学生信息
7. 退出系统
"""

import json
import prettytable  # https://www.cnblogs.com/Neeo/articles/14144637.html
dic = {}
PATH = 'E:\code\s31\day05-note\homework1\info.json'

def read_file():
    """
    :return: 初始化，将json文件中的学生信息读出来
    """
    with open(PATH, 'r', encoding='utf-8') as f:
        try:
            # 如果json文件不为空
            # tmp_dic = json.load(f)
            dic.update(json.load(f))
        except Exception as e:
            # print(e)
            pass

def save_file():
    """ 保存学生信息 """
    with open(PATH, 'w', encoding='utf-8') as f:
        # tmp = json.dumps(dic)
        # f.write(tmp)
        json.dump(dic, f)
        print('数据保存成功')

def add_info():
    """ 添加学生信息 """
    """
    {
    "12312": {"\u59d3\u540d": "xx", "\u5b66\u53f7": "12312", "y": 18, "s": 80, "e": 78}, 
    "12313": {"\u59d3\u540d": "xx", "\u5b66\u53f7": "12312", "y": 18, "s": 80, "e": 78}, 
    "12314": {"\u59d3\u540d": "xx", "\u5b66\u53f7": "12312", "y": 18, "s": 80, "e": 78}, 
    "12315": {"\u59d3\u540d": "xx", "\u5b66\u53f7": "12312", "y": 18, "s": 80, "e": 78}, 
    "12316": {"\u59d3\u540d": "xx", "\u5b66\u53f7": "12312", "y": 18, "s": 80, "e": 78}}
    """
    # 为了保证学号唯一，先获取所有学号
    while True:
        res1 = int(input('学号: ').strip())
        if res1 in dic:
            print('该学号已存在')
            continue
        res2 = input('姓名: ').strip()  # 刘开 123 12 68 32 34
        res4 = int(input('数学: ').strip())
        res5 = int(input('英语: ').strip())
        res6 = int(input('语文: ').strip())
        dic[res1] = {"姓名": res2, "学号": res1, "数学": res4, "英语": res5, "语文": res6}
        print('{}添加成功'.format(res2))
        break

def show_info():
    """ 根据学号查看学生信息 """
    while True:
        # tmp = [i['学号'] for i in score_sheet]
        cmd = int(input('根据学号查看信息:  '))
        if cmd in dic:
            table = prettytable.PrettyTable(['学号', '姓名', '语文', '数学', '英语'])
            table.add_row([
                dic[cmd]['学号'],
                dic[cmd]['姓名'],
                dic[cmd]['y'],
                dic[cmd]['s'],
                dic[cmd]['e'],
            ])
            print(table)
        else:
            print('查无学号')

def update_info():
    """ 根据学号更新学生信息 """
    while True:
        cmd = int(input('根据学号更新学生信息: ').strip())

        if cmd in dic:
            old_dic = dic[cmd]
            print(old_dic)
            # 思路，将能修改的学生信息都一一让其修改，然后进行更新
            # 问题，要注意用户不想修改的字段，回车即可

            res1, res3 = input('新的姓名: ').strip(), input('新的语文成绩: ').strip()
            res4, res5 = input('新的数学成绩: ').strip(), input('新的英语成绩: ').strip()
            res1 = res1 if res1 else dic[cmd]['姓名']
            res3 = res3 if res3 else dic[cmd]['y']
            res4 = res4 if res4 else dic[cmd]['s']
            res5 = res5 if res5 else dic[cmd]['e']
            dic[cmd] = {"姓名": res1, "学号": cmd, "s": int(res4), "e": int(res5), "y": int(res3)}
            # score_sheet[current_index] = new_dict
            print('old_dict: {}\nnew_dict:{}\nupdate successful'.format(old_dic, dic[cmd]))
            return
        else:
            print('查无学号')


def drop_info():
    """ 根据学号删除学生信息 """
    while True:
        cmd = input('根据学号删除学生信息/q退出:  ').strip()
        if cmd.upper() == 'Q':
            return
        if cmd.isdecimal():
            if cmd in dic:
                print(dic)
                # del dic[cmd]
                res = dic.pop(cmd)
                print('删除{}成功'.format(res['学号']))
            else:
                print('查无学号')
        else:
            print('请输入q或者数字!!!!')

def count_info():
    """ 统计信息：各学生的 平均成绩"""
    table = prettytable.PrettyTable(['学号', '姓名', '语文成绩', '数学成绩', '英语成绩', '平均成绩'])
    for k, v in dic.items():
        table.add_row([k, v['姓名'], v['y'], v['s'], v['e'], "%.2f" % ((v['y'] + v['s'] + v['e']) / 3)])
    print(table)


def q():
    """ 退出系统 """
    save_file()
    exit('退出系统辣')


def main():
    """ 入口函数 """
    # 获取学生列表
    read_file()
    while True:
        tmp_dict = {
            1: ['添加学生信息', add_info],
            2: ['根据学号查看学生信息', show_info],
            3: ['根据学号更新学生信息', update_info],
            4: ['根据学号删除学生信息', drop_info],
            5: ['统计信息', count_info],
            6: ['保存学生信息', save_file],
            7: ['退出系统', q],
        }
        for k, v in tmp_dict.items():
            print(k, v[0] )
        cmd = input('\n根据序号选择操作: ').strip()
        if cmd.isdigit():
            cmd = int(cmd)
            res = tmp_dict.get(cmd, None)
            if res:
                res[-1]()
            else:
                print('输入的数字超过范围!!!')
        else:
            print('请输入一个数字')


if __name__ == '__main__':
    main()