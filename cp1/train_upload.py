import psycopg2
import csv

conn = psycopg2.connect(
    host = 'jelani.db.elephantsql.com',
    database = 'dwghqzqc',
    user = 'dwghqzqc',
    password = 'eA0qInr1bk4Zynun6ix_SRIENlnuL_S7')

cur = conn.cursor()

cur.execute("""CREATE TABLE TRAIN_SET (
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

with open('DATA\TRAIN.csv', encoding = 'UTF-8') as csvfile:
    myReader = csv.reader(csvfile)
    next(myReader)

    enu = enumerate(myReader)
    total_row = len(open('DATA\TRAIN.csv', encoding = 'UTF-8').readlines())

    for idx, row in enu:
        cur.execute(f'INSERT INTO TRAIN_SET VALUES ({idx}, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', row)

        if idx % 1000 == 0:
            conn.commit()
            print(f'{idx}/{total_row} progressed')

conn.commit()
print(f'{total_row}/{total_row} progressed')

conn.close()