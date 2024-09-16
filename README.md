# ZiAssets

> 中文变量屎，有大错误，~~下个版本使用 [Node.js] 重写~~ 还是使用 Python 了。
> 
> [Node.js]: https://nodejs.org/zh-cn

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
$ tools/search.py data/lv0.json 字
字 -> 㝋J 字J 㝋. 字. 一. (5)
㝋J : 字J 𡧖J (2)
字J : 牸J 茡J 𡦂V 𡦙J 𡨸V 𣉬J 𣑑J 𥊐J 𦍺J 𧧕J 𪜸J 𪧚 𪰿 𫇊 𫡉 𫳘 𫿰 𭇬 𭸇 𮋩 𮪃 𱚂 𲂯 (23)
㝋. : 字. (1)
字. : 牸. 茡. 茡H 𡦂Q 𡦙. 𡧖T 𡨸Q 𡶻 𣉬. 𣑑T 𥊐. 𦍺. 𧧕. 𪜸. 𫃣 𫒛 𬇤 𭓆 𭓖 𭓙 (20)
一. : ⺊ ⺕ ⺝ ユ. 㐀 㐄J 㐆y 㒊J 㒨J 㒫 [实际上这汉字太多了，VSCode 都出 bug 了] (2886)
```

**请友善讨论，不要[评头论足]。对一些方面的请求（如不使用中文关键字）拒绝。**

[评头论足]: https://www.zdic.net/hans/%E8%AF%84%E5%A4%B4%E8%AE%BA%E8%B6%B3