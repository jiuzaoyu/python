import sqlite3

conn=sqlite3.connect('student.db')
curs=conn.cursor()

curs.execute('''
    create table student(
       id    TEXT  PRIMARY KEY,
       num   TEXT,
       name  TEXT
    )
    ''')

query='insert into student values(?,?,?)'
vals=['1','11','zwj']
curs.execute(query,vals)

querySql='select * from student'
print (querySql)
curs.execute(querySql)
names=[f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names,row):
        print ('%s: %s' % pair)
    print
    

conn.commit()
conn.close()
