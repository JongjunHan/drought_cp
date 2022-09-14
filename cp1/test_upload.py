import psycopg2
import csv

conn = psycopg2.connect(
    host = 'arjuna.db.elephantsql.com',
    database = 'godgfysz',
    user = 'godgfysz',
    password = 'rF7RTLYX2zEte4DWR7yb7KVc2f0FRAPj')

cur = conn.cursor()

cur.execute("""CREATE TABLE TEST_SET (
               id INT PRIMARY KEY,
               stnId INT,
               tm DATE,
               stnNm VARCHAR(16),
               avgTa FLOAT,
               minTa FLOAT,
               maxTa FLOAT,
               sumRn FLOAT,
               avgWs FLOAT,
               avgTd FLOAT,
               avgRhm FLOAT,
               avgPa FLOAT,
               avgTs FLOAT,
               SPI FLOAT);
               """)

with open('DATA\TEST.csv', encoding = 'UTF-8') as csvfile:
    myReader = csv.reader(csvfile)
    next(myReader)

    enu = enumerate(myReader)
    total_row = len(open('DATA\TEST.csv', encoding = 'UTF-8').readlines())

    for idx, row in enu:
        cur.execute(f'INSERT INTO TEST_SET VALUES ({idx}, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

        if idx % 1000 == 0:
            conn.commit()
            print(f'{idx}/{total_row} progressed')

conn.commit()
print(f'{total_row}/{total_row} progressed')

conn.close()