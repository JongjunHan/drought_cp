import psycopg2
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import pickle
import joblib

conn = psycopg2.connect(
    host = 'jelani.db.elephantsql.com',
    database = 'dwghqzqc',
    user = 'dwghqzqc',
    password = 'eA0qInr1bk4Zynun6ix_SRIENlnuL_S7')

cur = conn.cursor()
cur.execute("""SELECT * FROM TRAIN_SET;""")

result = cur.fetchall()

df = pd.DataFrame(result, columns = ['id', 'stnId', 'tm', 'stnNm', 'avgTa', 'minTa', 'maxTa', 'sumRn', 'avgWs', 'avgTd', 'avgRhm', 'avgPa', 'avgTs', 'SPI'])

data1 = df['SPI'] == 3
data11 = df[data1].sample(n = 10000)
data2 = df['SPI'] == 4
data12 = df[data2].sample(n = 10000)
data3 = df['SPI'] == 5
data13 = df[data3].sample(n = 4000)
data4 = df['SPI'] >= 6
data14 = df[data4]
data5 = df['SPI'] <= 2
data15 = df[data5]

data_all = pd.concat([data15, data11, data12, data13, data14], ignore_index = True)

new_range = {'SPI' : {0 : 0, 1 : 0, 2 : 0, 3 : 1, 4 : 1, 5 : 1, 6 : 1, 7 : 1}}

data = data_all.replace(new_range)

train = data.drop(['id', 'tm', 'stnNm'], axis = 1)

X_train = train.drop('SPI', axis = 1)
y_train = train['SPI']

sc = StandardScaler()

X_train_sc = sc.fit_transform(X_train)

model = RandomForestClassifier(n_estimators = 300, max_depth = 20, random_state = 42)

model.fit(X_train_sc, y_train)

# with open('./modeling/model.pkl', 'wb') as pickle_file:
#     pickle.dump(model, pickle_file, pickle.HIGHEST_PROTOCOL)

joblib.dump(model, 'model.pkl', compress = 3)