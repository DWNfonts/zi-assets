#!/usr/bin/env python3

# tools/search.py - 反查 CLI 程序
# 使用方法：python tools/search.py [处理后 JSON 部件表] [字] [狂搜等级]
# 注意：狂搜等级未经过优化，如果狂搜等级提升，意味着该程序将会花很长时间处理部件信息。谨慎调试。
# zi-assets 的一部分 - © DWNfonts。查看 LICENSE.md 知晓授权信息。

# *未为版本 2 准备好*

import sys, json


def 搜索(部件表, 字, 狂搜等级=0, 调试=False):
    字头表 = list(部件表)
    要搜索部件 = set()
    for 字头 in 字头表:
        if 字头.startswith(字):
            要搜索部件 = 要搜索部件.union(set([字头] + 部件表[字头]))
    结果 = {"->": [字, list(要搜索部件)]}
    if 调试:
        print("搜索 %s" % (要搜索部件), file=sys.stderr)
    for 部件 in 要搜索部件:
        for 字头 in 字头表:
            if 部件 in 部件表[字头]:
                try:
                    结果[部件] += [字头]
                except Exception:
                    结果[部件] = [字头]
        for 天 in range(狂搜等级):
            if 调试:
                print(
                    "部件 %s，正在进行第 %d 次遍历……" % (部件, 天 + 1), file=sys.stderr
                )
            try:
                for 项 in 结果[部件]:
                    for 字头 in 字头表:
                        if 项 in 部件表[字头]:
                            try:
                                结果[部件] += [字头]
                            except Exception:
                                结果[部件] = [字头]
            except:
                print(
                    "该 JSON 没有 %s 部件。是子集化的 IDS 吗？" % 部件, file=sys.stderr
                )
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
    if len(sys.argv) != 3 and len(sys.argv) != 4:
        raise Exception("给定的参数太多或太少。")
    try:
        狂搜等级 = int(sys.argv[3])
    except Exception:
        狂搜等级 = 0
    with open(sys.argv[1]) as 文件:
        JSON内容 = 文件.read()
        处理内容 = json.loads(JSON内容)
        print(美化(搜索(处理内容, sys.argv[2], 狂搜等级, True)))
