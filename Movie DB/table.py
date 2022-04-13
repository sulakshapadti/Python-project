import sqlite3
con=sqlite3.connect('movieDB.db')
c=con.cursor()
#Below given query creates a table named as MOVIE
c.execute("""CREATE TABLE MOVIE
           (NAME TEXT NOT NULL, 
           ACTOR TEXT NOT NULL, 
           ACTRESS TEXT NOT NULL,
           DIRECTOR TEXT NOT NULL,
           YEAR_OF_RELEASE INT NOT NULL);""")
con.commit()

con.close()
