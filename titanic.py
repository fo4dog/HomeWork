
import csv, sqlite3
to_db = []
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("CREATE TABLE t (MonthReport, Calls);")
c= 0
d = 0
month = []
new_manth = ''
summ = 0
with open('data-5284-2019-01-28.csv') as fin:

    dr = csv.DictReader(fin, delimiter=';')
    for i in dr:
        to_db = [(i.get("MonthReport"), i.get('Calls'))]
        cur.executemany("INSERT INTO t (MonthReport, Calls) VALUES (?, ?);", to_db)
for row in con.execute('SELECT Calls FROM t'):
    c+=(int(row[0]))
for row in cur.execute('select MonthReport, Calls from t'):
    if row[0][-1] == '7' and row[0][-2] == '1':
        print(row[0], ':', row[1])
for row in cur.execute('select MonthReport, Calls from t group by MonthReport'):

    if row[0][:-5] != new_manth :
        if new_manth != '':
            month.append([new_manth, summ])
        new_manth = row[0][:-5]
        summ = 0
    else:
        summ += int(row[1])
    month.append([new_manth, summ])
month = dict(month)
con.commit()
con.close()
print('вызовов за все года',c)
print(month)