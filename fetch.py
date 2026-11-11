import sqlite3

# Connect to the database
conn = sqlite3.connect('companydb.sqlite')
cursor = conn.cursor()


# --- Fetch all companies ---
cursor.execute('SELECT * FROM company')
companies = cursor.fetchall()

print('All companies:')
for company in companies:
    print(company)


# --- Fetch all people ---
cursor.execute('SELECT * FROM person')
people = cursor.fetchall()

print('\nAll people:')
for person in people:
    print(person)


# --- Fetch offers for a specific company ---
company_id = 1

cursor.execute('''SELECT p.person_name, c.company_name, o.role, o.salary, o.offered
    FROM person p, company c, offer o
    WHERE p.person_id = o.person_id
    AND c.company_id = o.company_id
    AND c.company_id = ?''', (company_id,))

results = cursor.fetchall()

print(f'\nOffers for company_id {company_id}:')
for row in results:
    print(row)


# --- Wrap it in a function ---
def get_offers_by_company(company_id):
    cursor.execute('''
        SELECT p.person_name, c.company_name, o.role, o.salary, o.offered
        FROM person p, company c, offer o
        WHERE p.person_id = o.person_id
        AND c.company_id = o.company_id
        AND c.company_id = ?
    ''', (company_id,))
    return cursor.fetchall()


print('\nGoogle offers:')
for row in get_offers_by_company(1):
    print(row)

print('\nAmazon offers:')
for row in get_offers_by_company(2):
    print(row)


# Close the connection
conn.close()