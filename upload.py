import pyodbc, os
cnxn = pyodbc.connect(r'DRIVER={ODBC Driver 13 for SQL Server};'
                      r'SERVER=DESKTOP\SQLEXPRESS;'
                      r'DATABASE=twitter;'
                      r'UID=jason;'
                      r'PWD=jason')

cursor = cnxn.cursor()

cursor.execute("""BULK INSERT twitter.dbo.tweets FROM 'E:/TwitterBot/tweets.csv' WITH (FIELDTERMINATOR = '*!*', ROWTERMINATOR = '\n' )""")
cnxn.commit()
os.remove('E:/TwitterBot/tweets.csv')
