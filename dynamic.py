import sqlite3

conn = sqlite3.connect('companydb.sqlite')
cursor = conn.cursor()


# cursor.description gives you column names after a query runs
# You do not need to know the column names upfront

def run_query(sql, params=()):
    cursor.execute(sql, params)
    columns = [description[0] for description in cursor.description]
    rows = cursor.fetchall()
    return [dict(zip(columns, row)) for row in rows]


# Works on any query, any table, any number of columns
results = run_query('''
    SELECT p.person_name, p.experience, c.company_name, o.role, o.salary
    FROM person p, company c, offer o
    WHERE p.person_id = o.person_id
    AND c.company_id = o.company_id
    AND o.offered = 1
''')

for row in results:
    print(row)


conn.close()
