# -*- coding:utf8 -*-

import sqlite3
from jieba import analyse
from textrank4zh import TextRank4Keyword

from config import dbfile

def extract_keyword():
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    cursor = c.execute("SELECT question_id,question FROM question")
    rows = c.fetchall()
    for row in rows:
        print row[0]
        keywords = text_rank(row[1].replace(' ', ''))
        c.execute('UPDATE question SET keywords=? WHERE question_id=?', \
            (keywords,row[0]))
        conn.commit()

    conn.close()

def text_rank(question):
    tr4w = TextRank4Keyword()
    tr4w.analyze(text=question, lower=True)
    return ' '.join(tr4w.words_no_stop_words[0])

if __name__ == '__main__':
    extract_keyword()
