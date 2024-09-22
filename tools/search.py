#!/usr/bin/env python3

# tools/search.py - 反查 CLI 程序 / 库

# 使用方法：python tools/search.py [命令] [字] [选项] < [JSON 文件]
# 命令：「反」=「单字反差」；「搜」=「部件检索」（未实现）
# 选项：-遍x：遍历 x 遍；-线y：进程增加（也未实现）

# 注意：狂搜等级未经过优化，如果狂搜等级提升，意味着该程序将会花很长时间处理部件信息。谨慎调试。
# zi-assets 的一部分 - © DWNfonts。查看 LICENSE.md 知晓授权信息。

import sys, json


def 反查(输入字典, 输入汉字, 遍历次数=0, 调试=False):
    输出 = {"欲拼部件组": [], "部件": {}, "汉字": 输入汉字}
    欲拼部件组 = []
    for 项 in 输入字典["拆"]:
        if 项.startswith(输入汉字):
            欲拼部件组 += [项] + 输入字典["拆"][项]
    输出["欲拼部件组"] = 欲拼部件组
    for 欲拼部件 in 欲拼部件组:
        try: 输出["部件"][欲拼部件] = 输入字典["拼"][欲拼部件]
        except Exception:
            if 调试:
                print("%s 搜不出来。" % 欲拼部件, file=sys.stderr)
    for 遍历号 in range(遍历次数):
        if 调试:
            print("进行第 %d 次遍历。" % 遍历号, file=sys.stderr)
        for 项 in list(输出["部件"]):
            输出列表 = 输出["部件"][项]
            for 子部件 in 输出["部件"][项]:
                try:
                    输出列表 += 输入字典["拼"][子部件]
                except Exception:
                    if 调试:
                        print("%s 字不可搜。" % 子部件, file=sys.stderr)
            输出列表 = list(set(输出列表))
            输出列表.sort()
            输出["部件"][项] = 输出列表

    return 输出


def 美化(反查字典):
    输出 = "%s -> %s\n" % (反查字典["汉字"], " ".join(反查字典["欲拼部件组"]))
    for 项 in list(反查字典["部件"]):
        输出 += "%s : %s (%d)\n" % (
            项,
            " ".join(反查字典["部件"][项]),
            len(" ".join(反查字典["部件"][项])),
        )
    return 输出


if __name__ == "__main__":
    输入 = json.load(sys.stdin)
    match sys.argv[1]:
        case "反" | "单字反查":
            try:
                遍历次数 = int(sys.argv[3])
            except Exception:
                遍历次数 = 0
            print(美化(反查(输入, sys.argv[2], 遍历次数, 调试=True)))
        case _:
            raise Exception("非法语句。")
