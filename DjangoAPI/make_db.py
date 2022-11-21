import pandas as pd
import sqlite3

df = pd.read_excel('tabela.xlsx')

# print(df)

db = sqlite3.connect('db.sqlite3')
# db.execute('CREATE TABLE IF NOT EXISTS products (aliquita number, name text, ncm text, fecoep number)')
# c = db.cursor()
df.to_sql('AliquotaApp_produtos', db, if_exists='append', index=False)
# df = pd.read_excel('tabela.xlsx', sheet_name=None)
# for table, df in df.items():
#      df.to_sql('AliquotaApp_produtos', db)

