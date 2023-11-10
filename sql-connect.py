import pyodbc
# cnxn = pyodbc.connect("Driver={SQL Server};"
#                       "Server=utegration.database.windows.net;"
#                       "Database=Utegration_Uplan;"
#                       "Trusted_Connection=yes;")


# cursor = cnxn.cursor()
# cursor.execute('SELECT * FROM dbo.Leave')

# for row in cursor:
#     print('row = %r' % (row,))

for driver in pyodbc.drivers():
    print(driver)
