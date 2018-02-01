# -*- coding:utf8 -*-

import argparse
import sqlite3
import cgi

from config import dbfile

def gen_tpl(file):
    with open(file, 'w') as outf:
        outf.write('<?xml version="1.0" encoding="UTF-8"?>\n<aiml version="1.0">\n'.encode('utf8'))

        conn = sqlite3.connect(dbfile)
        c = conn.cursor()
        cursor = c.execute('SELECT question_id,keywords FROM question')
        rows = c.fetchall()
        for row in rows:
            print row[0]
            if row[1] == '': continue
            cursor = c.execute('SELECT answer FROM answer WHERE question_id=?', (row[0],))
            answers = c.fetchall()
            if len(answers) == 1:
                outf.write(('<category><pattern>* ' + cgi.escape(row[1].replace(' ', ' * '))
                    + ' *</pattern><template>' + cgi.escape(answers[0][0]) + '</template></category>\n').encode('utf8'))
            elif len(answers) > 1:
                outf.write(('<category><pattern>* ' + cgi.escape(row[1].replace(' ', ' * ')) 
                    + ' *</pattern><template><random>').encode('utf8'))
                for answer in answers:
                    outf.write(('<li>' + cgi.escape(answer[0]) + '</li>').encode('utf8'))
                outf.write('</random></template></category>\n'.encode('utf8'))

        conn.close()
        outf.write('</aiml>\n'.encode('utf8'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', required=True,
        help='file to store aiml template.')
    args = parser.parse_args()
    gen_tpl(args.file)
