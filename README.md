# Russian-news-frequency
俄语新闻文本词频统计与分析 - 使用 Python 进行文本清洗、词形归并、词频统计并生成词云

功能

- 文本清洗（正则去除非俄语字符、数字、标点）
- 停用词过滤（除去常规停用词，还专门添加了这几篇新闻统一发布的报社与月份等无重大意义的词汇）
- 词形归并（pymorphy3，将不同语法形式统一为词典原形）
- 词频统计（Counter）
- 柱状图（matplotlib)
- 词云可视化（wordcloud）

技术栈

Python, re, collections, pymorphy3, wordcloud, matplotlib

运行方法

1. 安装依赖：'py -m pip install pymorphy3 wordcloud matplotlib'
2. 将俄语新闻文本保存为 'news.txt'（UTF-8 编码）
3. 运行 'py rnf.py'
4. 查看终端输出的词频统计结果，并打开生成的'top20.png'和 'russian_wordcloud.png'
