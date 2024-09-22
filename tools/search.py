#!/usr/bin/env python3

# tools/search.py - 反查 CLI 程序 / 库

# 使用方法：python tools/search.py [命令] [字] [选项] < [JSON 文件]
# 命令：「反」=「单字反差」；「搜」=「部件检索」（未实现）
# 选项：-遍x：遍历 x 遍；-线y：进程增加（也未实现）

# 注意：狂搜等级未经过优化，如果狂搜等级提升，意味着该程序将会花很长时间处理部件信息。谨慎调试。
# zi-assets 的一部分 - © DWNfonts。查看 LICENSE.md 知晓授权信息。

import sys, json


def 反查(输入字典, 输入汉字, 遍历次数, 线程数):
    输出 = {"欲拼部件组": [], "部件": {}}
    欲拼部件组 = 输入字典["拆"][输入汉字]
    输出["欲拼部件组"] = 欲拼部件组
    for 欲拼部件 in 欲拼部件组:
        输出["部件"][欲拼部件] = 输入字典["拼"][欲拼部件]
    return 输出

def 美化(反查字典):
    return str(反查字典)

if __name__ == "__main__":
    输入 = json.load(sys.stdin)
    match sys.argv[1]:
        case "反" | "单字反查":
            print(str(反查(输入,sys.argv[2],0,0)))
        case _:
            raise Exception("非法语句。")
