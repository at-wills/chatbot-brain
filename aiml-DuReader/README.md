## DuReader 数据集清洗

### 整理到 sqlite 中

将预处理过（preprocessed）的训练集整理到 sqlite 中

```shell
$ cd aiml-DuReader
$ python gen_db.py --files ../data/DuReader/preprocessed/trainset/search.train.json ../data/DuReader/preprocessed/trainset/zhidao.train.json
```

最终数据表格式示例：

| question_id | question | document | answer |
| ----------- | -------- | -------- | ------ |
| amount      | 201574   | 946880   | 421703 |
| avg len     | 5        | 394      | 67     |

| answer_id | question_id | answer |
| --------- | ----------- | ------ |
| amount    | 201574      | 946880 |
| avg len   | 5           | 394    |

### 关键词抽取

利用 TextRank 算法，对于每个 question 的中文文本进行关键词抽取

TextRank 实现：textrank4zh（[https://github.com/letiantian/TextRank4ZH](https://github.com/letiantian/TextRank4ZH)）

```shell
$ cd aiml-DuReader
$ python extract_keyword.py
```

抽取结果示例：

| question_id | question | keywords |
| ----------- | -------- | -------- |
| amount      | 201574   | 946880   |
| avg len     | 5        | 394      |

### 问题短文本聚类

[GSDMM](https://github.com/rwalk/gsdmm)

## AIML 模板生成

AIML 中对于每个问答对以 \<pattern>\<template> 对表示，即问题放在 \<pattern> 部分，回答放在 \<template>。数据集中存在一个问题多个回答的情形，将采用 \<random>\<li> 来随机选取一个回答返回给提问者

为了提供提问与模板中问题的匹配率，\<pattern> 部分将只保留原语料问题中的关键词，例如

```xml
# 抽取关键词为“”、“”、“”

<pattern></pattern>
```
