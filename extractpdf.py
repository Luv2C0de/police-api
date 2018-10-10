import PyPDF2
import re
import sqlite3
from crime import Crime

conn = sqlite3.connect(':memory:')

c = conn.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS crimes(
            title text,
            police_number text,
            address text,
            district text
            )""")


def insert_crime(crime):
    with conn:
        c.execute("INSERT INTO crimes VALUES (:title, :police_number, :address, :district)", {
                  'title': crime.title, 'police_number': crime.police_number, 'address': crime.address, 'district': crime.district})


def get_crime_by_district(district):
    c.execute("SELECT * FROM crimes WHERE district=:district",
              {'district': district})
    # print(c.fetchall())
    return c.fetchall()


def get_crime_by_street(street):
    c.execute("SELECT * FROM crimes WHERE address LIKE :street",
              {'street': '%' + street + '%'})
    # print(c.fetchall())
    return c.fetchall()


def get_count_by_street(street):
    c.execute("SELECT COUNT(address) FROM crimes WHERE address LIKE :street",
              {'street': '%' + street + '%'})
    # print(c.fetchall())
    return c.fetchall()


def get_count_by_crime(crime, street):
    c.execute("SELECT COUNT(title) FROM crimes WHERE title LIKE :crime AND address LIKE :street",
              {'crime': '%' + crime + '%', 'street': '%' + street + '%'})
    # print(c.fetchall())
    return c.fetchall()


create_table()

for i in range(1, 30):

    file_name = f'test{i}.pdf'
    # file_name = 'test12.pdf'

    try:
        # print('hello')
        pdf_file = open(file_name, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        page = read_pdf.getPage(0)
        page_content = page.extractText()

        page_content = ' '.join(page_content.split())

        records = re.findall(r'Assault.*?District', page_content)

        for record in records:

            pattern = re.compile(r'^[^\(]+')
            matchedPattern = pattern.search(record)

            title = matchedPattern.group(0)

            record = record[len(title):]

            title = title.rstrip()

            pattern = re.compile(r'\((.*?)\)')
            matchedPattern = pattern.search(record)

            count = matchedPattern.group(0)

            police_number = matchedPattern.group(1)

            record = record[len(count):].lstrip()

            pattern = re.compile(r'^[^\,]+')
            matchedPattern = pattern.search(record)

            address = matchedPattern.group(0)

            record = record[(len(address)+2):]

            district = record

            district = district.rstrip()

            # print(district)

            crime = Crime(title, police_number, address, district)

            insert_crime(crime)

            # print(crime)

        pdf_file.close()
        # pdf_file.close()
    except Exception:
        print("not working")

print(get_crime_by_district('Park District'))
# print(get_crime_by_street('Block'))
# print(get_count_by_street('Block'))
# print(get_count_by_crime('Assault', 'Block'))


# print(page_content)
