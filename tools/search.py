#!/usr/bin/env python3

# tools/search.py - 反查 CLI 程序
# 使用方法：python tools/search.py [处理后 JSON 部件表] [字]
# zi-assets 的一部分 - © DWNfonts。查看 LICENSE.md 知晓授权信息。

import sys, json


def 搜索(部件表, 字):
    字头表 = list(部件表)
    要搜索部件 = set()
    for 字头 in 字头表:
        if 字头.startswith(字):
            要搜索部件 = 要搜索部件.union(set([字头] + 部件表[字头]))
    结果 = {"->": [字, list(要搜索部件)]}
    for 部件 in 要搜索部件:
        for 字头 in 字头表:
            if 部件 in 部件表[字头]:
                try:
                    结果[部件] += [字头]
                except Exception:
                    结果[部件] = [字头]
    return 结果


def 美化(结果):
    输出 = "%s -> %s (%d)\n" % (
        结果["->"][0],
        " ".join(结果["->"][1]),
        len(结果["->"][1]),
    )
    for 字头 in 结果:
        if 字头 == "->":
            pass
        else:
            输出 += "%s : %s (%d)\n" % (字头, " ".join(结果[字头]), len(结果[字头]))
    return 输出


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("给定的参数太多或太少。")
    with open(sys.argv[1]) as 文件:
        JSON内容 = 文件.read()
        处理内容 = json.loads(JSON内容)
        print(美化(搜索(处理内容, sys.argv[2])))
