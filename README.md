# chatbot 语料库构建

## 数据源 —— DuReader

### 基本信息

该数据源是 Baidu Research 依据“百度搜索”和“百度知道”整理的中文问答数据集，其来源于百度 WebQA [http://idl.baidu.com/WebQA.html](http://idl.baidu.com/WebQA.html)

DuReader 下载地址为 [http://ai.baidu.com/broad/introduction?dataset=dureader](http://ai.baidu.com/broad/introduction?dataset=dureader)

|         | question | document | answer |
| ------- | -------- | -------- | ------ |
| amount  | 201574   | 946880   | 421703 |
| avg len | 5        | 394      | 67     |

下面给出一个例子：

```
{
    "question_id": 186358,
    "question_type": "YES_NO",
    "question": "上海迪士尼可以带吃的进去吗",
    "documents": [
        {
            "paragraphs": ["text paragraph 1", "text paragraph 2"],
            "title": "上海迪士尼可以带吃的进去吗",
            "bs_rank_pos": 1,
            "is_selected": True
        },
        # ...
    ],
    "answers": [
        "完全密封的可以，其它不可以。",                                        # answer1
        "可以的，不限制的。只要不是易燃易爆的危险物品，一般都可以带进去的。",  # answer2
        "罐装婴儿食品、包装完好的果汁、水等饮料及包装完好的食物都可以带进乐园，但游客自己在家制作的食品是不能入园，因为自制食品有一定的安全隐患。"        # answer3
    ]
}
```

### 数据获取

```shell
$ cd data
$ ./download.sh
```

下载得到的数据分为 raw 和 preprocessed 两部分，preprocessed 的数据是经过 raw 预处理得到的。预处理的主要工作是，对于 question、answers 等中文文本作分词处理，处理的结果分别放在  segmented_question、segmented_answers 中

### 清洗数据

将预处理过（preprocessed）的训练集整理到 sqlite 中

```shell
$ cd code
$ python gen_db.py --files ../data/preprocessed/trainset/search.train.json ../data/preprocessed/trainset/zhidao.train.json
```
