## DuReader 数据集清洗

### 整理到 sqlite 中

将预处理过（preprocessed）的训练集整理到 sqlite 中

```shell
$ cd aiml-DuReader
$ python gen_db.py --files ../data/DuReader/preprocessed/trainset/search.train.json ../data/DuReader/preprocessed/trainset/zhidao.train.json
```

最终数据表格式示例：

| question_id | question | question_type | fact_or_opinion |
| ----------- | -------- | ------------- | --------------- |
| 0           | 绣眉有哪几种   | ENTITY        | FACT            |
| 1           | 实习的目的    | DESCRIPTION   | OPINION         |

| answer_id | question_id | answer                                   |
| --------- | ----------- | ---------------------------------------- |
| 79        | 0           | 绣眉的五种基本方法：1、雕润眉；2、平面绣眉；3、点状绣眉；4、立体绣眉；5、仿真立体绣眉。 |
| 80        | 1           | 1．为了将自己所学知识运用在实践中，在实践中巩固自己的知识，调节理论与实践之间的关系，培养实际工作能力和分析能力，以达到学以致用的目的。2．获得更多与自己专业相关的知识，扩宽知识面，增加社会阅历。3．接触更多的人，在实践中锻炼胆量，提升自己的沟通能力和其他社交能力。4．培养更好的职业道德，树立好正确的职业道德观。 |

### 关键词抽取

利用 TextRank 算法，对于每个 question 的中文文本进行关键词抽取

TextRank 实现：textrank4zh（[https://github.com/letiantian/TextRank4ZH](https://github.com/letiantian/TextRank4ZH)）

```shell
$ cd aiml-DuReader
$ python extract_keyword.py
```

抽取结果示例：

| question_id | question | keywords      |
| ----------- | -------- | ------------- |
| 0           | 绣眉有哪几种   | “绣”、“眉”、“哪几种” |
| 1           | 实习的目的    | “实习”、“目的”     |

### 问题短文本聚类

[GSDMM](https://github.com/rwalk/gsdmm)

## AIML 模板生成

AIML 中对于每个问答对以 \<pattern>\<template> 对表示，即问题放在 \<pattern> 部分，回答放在 \<template>。数据集中存在一个问题多个回答的情形，将采用 \<random>\<li> 来随机选取一个回答返回给提问者

```shell
$ cd aiml-DuReader
$ python gen_tpl.py --file brain.aiml
```

为了提供提问与模板中问题的匹配率，\<pattern> 部分将只保留原语料问题中的关键词，例如

```
question：实习的目的 # 抽取关键词为“实习”、“目的”
<pattern>* 实习 * 目的 *</pattern>
```
