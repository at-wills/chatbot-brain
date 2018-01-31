# -*- coding:utf8 -*-

import argparse
import json
import sqlite3

from config import dbfile

def gen_db(files):
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute('''CREATE TABLE question
        (question_id INTEGER PRIMARY KEY NOT NULL,
        question TEXT,
        question_type TEXT,
        fact_or_opinion TEXT,
        keywords TEXT,
        category TEXT);''')
    c.execute('''CREATE TABLE answer
        (answer_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        question_id INTEGER,
        answer TEXT);''')
    conn.commit()
    conn.close()

    for f in files:
        with open(f, 'r') as fin:
            for line in fin:
                obj = json.loads(line.strip())
                add_question(obj)

def add_question(question):
    print question['question_id']
    conn = sqlite3.connect(dbfile)
    c = conn.cursor()
    c.execute('INSERT INTO question(question_id,question,question_type,fact_or_opinion) \
        VALUES(?,?,?,?)', (question['question_id'],' '.join(question['segmented_question']), \
        question['question_type'],question['fact_or_opinion']))
    for answer in question['answers']:
        c.execute('INSERT INTO answer(question_id,answer) VALUES(?,?)', \
            (question['question_id'],answer))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', nargs='+', required=True,
            help='file list to generate template from.')
    args = parser.parse_args()
    gen_db(args.files)
