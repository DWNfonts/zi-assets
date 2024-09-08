#!/usr/bin/env python3

# libids.py - 读取白易版 IDS 工具。
# © DWNfonts。用 3 语句 BSD 协议授权。详情 LICENSE.md。


def 分离字符串(字符串):
    # 该函数会默认你将 IDS 以类似此方法整理：
    # 处理前（𥫹V）：⿱𥫗.⿻[,,r]丿⿱冖⿻㇈.丶.(V)
    # 处理后：𥫗.⿻[,,r]丿⿱冖⿻㇈.丶.
    # 这么处理，该函数会 *初步* 分离出其部件。
    粗拆 = []
    for 天 in range(len(字符串)):
        字 = 字符串[天]
        if 字 == "}":
            粗拆[-1] += 字
        elif 字符串[天 - 1] == "}" and 字 in "⿾⿿⿰⿱⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽⿲⿳":
            粗拆[-1] += 字
        elif 字 != "" and 字 in "0123456789.BGHJKMPQSTUVabcdefghjlmnpqrstuvwxyz()[],-_":
            粗拆[-1] += 字
        else:
            粗拆.append(字)

    IDC = ["⿾⿿", "⿰⿱⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽", "⿲⿳"]
    甲 = 1
    结果 = [""]
    for 天 in range(len(粗拆)):
        字 = 粗拆[天]
        甲 -= 1
        if set(字) & set(IDC[0]):
            甲 += 1
        elif set(字) & set(IDC[1]):
            甲 += 2
        elif set(字) & set(IDC[2]):
            甲 += 3
        else:
            甲 += 0
        if 甲 == 0:
            甲 = 1
            结果[-1] += 字
            结果.append("")
        else:
            结果[-1] += 字
    if 结果[-1] == "":
        结果.pop(-1)
    return 结果


def 拆IDS(IDS):
    # 认为此 IDS 在 IDS 上可拆（成汉字，而非调用数据拆成笔画）：
    # 以 "{xxx}" + IDC + "[yyy]" 开头。
    # 但实际上，仅需要搜索字符串的 IDC 就行。
    甲 = ""
    结果 = {}
    IDC部分处理完了吗 = False
    for 天 in range(len(IDS)):
        字 = IDS[天]
        甲 += 字
        if 字 in "⿾⿿⿰⿱⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽⿲⿳" and not IDC部分处理完了吗:
            结果["拼合方式"] = 甲
            if IDS[天 + 1] != "[":
                甲 = ""
                IDC部分处理完了吗 = True
        elif 字 == "]" and not IDC部分处理完了吗:
            结果["方括号"] = 甲
            甲 = ""
            IDC部分处理完了吗 = True
        elif 天 + 1 == len(IDS):
            结果["部件"] = 分离字符串(甲)
    return 结果


def 狂拆IDS(IDS):
    拆了的IDS = 拆IDS(IDS)
    for 天 in range(len(拆了的IDS["部件"])):
        部件 = 拆了的IDS["部件"][天]
        if set(部件) & set("⿾⿿⿰⿱⿴⿵⿶⿷⿸⿹⿺⿻⿼⿽⿲⿳"):  # 部件可拆
            拆了的IDS["部件"][天] = 狂拆IDS(部件)
    return 拆了的IDS
