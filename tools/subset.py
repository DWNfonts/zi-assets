#!/usr/bin/env python3

# tools/subset.py - 将 IDS 文件子集化。
# 使用方法：python tools/subset.py [字表文件/文本] < [未子集化 IDS 文本] > [子集化 IDS 文本]
# zi-assets 的一部分 - © DWNfonts。查看 LICENSE.md 知晓授权信息。

import sys

if __name__ != "__main__":
    raise Exception("__name__ 不等于 __main__。不要导入该脚本。")

if len(sys.argv) != 2:
    raise Exception("给定的参数太多或太少。")

字表 = sys.argv[1]

try:
    with open(字表) as 文件:
        字表 = 文件.read()
except Exception:
    pass
未子集化IDS = sys.stdin.read()

for 行 in 未子集化IDS.splitlines():
    if 行.split("\t")[0] in 字表:
        print(行)
