# ZiAssets

这是一款通过汉字的相应部件反查其他部件的库/脚本。

使用最新的 [Python] 来运行。

[Python]: https://www.python.org

## 用法

```bash
# 准备
git clone https://github.com/DWNfonts/zi-assets.git
cd zi-assets
git clone https://github.com/yi-bai/ids.git
tools/idssplit.py < ids/ids_lv0.txt > data/lv0.json
tools/idssplit.py < ids/ids_lv1.txt > data/lv1.json
tools/idssplit.py < ids/ids_lv2.txt > data/lv2.json
```

```
$ # 使用方法：python tools/search.py [命令] [字] [选项] < [JSON 文件]
$ # 命令：「反」=「单字反差」；「搜」=「部件检索」（未实现）
$ # 选项：-遍x：遍历 x 遍；-线y：进程增加（也未实现）
$ tools/search.py 反 口 < data/lv0.json
$ tools/search.py 反 口 1 < data/lv0.json
```

**请友善讨论，不要[评头论足]。对一些方面的请求（如不使用中文关键字）拒绝。**

[评头论足]: https://www.zdic.net/hans/%E8%AF%84%E5%A4%B4%E8%AE%BA%E8%B6%B3