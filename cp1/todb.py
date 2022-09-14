import pandas as pd
import sqlite3

df1 = pd.read_csv('DATA\TRAIN.csv', encoding = 'UTF-8')
df2 = pd.read_csv('DATA\TEST.csv', encoding = 'UTF-8')

con1 = sqlite3.connect('DB\TRAIN.db')
con2 = sqlite3.connect('DB\TEST.db')

df1.to_sql('DB1', con1)
df2.to_sql('DB2', con2)