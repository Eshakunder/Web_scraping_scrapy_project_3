# #basic database operations using sqlite3 module in python.
# import sqlite3

# conn = sqlite3.connect('myquotes.db')#connect to the database 
# #if it doesn't exist, it will be created .
# #run using triangle icon.
# curr = conn.cursor() #cursor helps to take advatage of all the functionality of sql.

# #to write a query -> curr.execute()

# curr.execute("""create table quotes_tb(
#              title  text ,
#              author text ,
#              tag text 
#              )""")
# curr.execute("""insert into quotes_tb values(
#              'A day without sunshine is like, you know, night.',
#              'Steve Martin',
#              'humor, obvious, simile'
#              )""")
# conn.commit() # to run the query 
# conn.close()