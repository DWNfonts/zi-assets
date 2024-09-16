#!/usr/bin/env python3

# tools/idssplit.py - 将 IDS 文件的部件提取出来。
# 使用方法：python tools/idssplit.py < [IDS 文本] > [输出 JSON]
# zi-assets 的一部分 - © DWNfonts。查看 LICENSE.md 知晓授权信息。

import sys, re, json

if __name__ != "__main__":
    raise Exception("__name__ = __main__ only")

IDC正则 = '(\\{[^ ].*?\\})?[\\u2ff0-\\u2fff](\\[[^ ].*?\\])?|^\\{[^ ].*?\\}'
汉字正则 = '#\\([^ ].*?\\)|[^ ][.0123456789BGHJKMPQSTUVabcdefghjlmnpqrstuvwxyz]*'

输出 = {}
数据 = sys.stdin.read()
for 行 in 数据.splitlines():
    汉字 = 行.split("\t")[0]
    for 说法 in 行.split("\t")[1:]:
        for 地区字形 in 说法.split(";"):
            try:
                if 地区字形.split("(")[-2][-1] == "#":
                    总地区 = [""]
                    序列 = 地区字形
                elif "(" in 地区字形:
                    总地区 = 地区字形.split("(")[-1][:-1].split(",")
                    序列 = "(".join(地区字形.split("(")[:-1])
                else:
                    总地区 = [""]
                    序列 = 地区字形
            except Exception:
                总地区 = [""]
                序列 = 地区字形
            for 地区 in 总地区:
                剩部件序列 = re.sub(IDC正则, "", 序列)
                部件列表 = set(re.findall(汉字正则, 剩部件序列))
                try:
                    输出[汉字 + 地区] = 输出[汉字].union(部件列表)
                except:
                    输出[汉字 + 地区] = 部件列表

for 项 in list(输出):
    输出[项] = list(输出[项])

print(json.dumps(输出))
