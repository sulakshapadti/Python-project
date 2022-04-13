import sqlite3

#connection to database
con=sqlite3.connect('movieDB.db')
c=con.cursor()
#number of values to be inserted ex:n=3 user has to enter 3 movie details
n=int(input('Enter number of values: '))
for i in range(0,n):
    name=input("Enter movie name: ")
    actor=input("Enter actor name: ")
    actress=input("Enter actress name: ")
    director=input("Enter Director name: ")
    yof=int(input("Enter year of realease: "))
    c.execute("""INSERT INTO MOVIE(NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE)\
    VALUES(?,?,?,?,?)""",(name,actor,actress,director,yof))
print("\n\n\n")
#Below query prints all the values in the table MOVIE
row=c.execute('SELECT * FROM MOVIE')
for i in row:
    print("***********************")
    print("Movie Name:"+i[0])
    print("Actor:"+i[1])
    print("Actress:"+i[2])
    print("Director:"+i[3])
    print("Year of release:",i[4])
    print("***********************\n\n\n")

#Below given query prints the movie details based on the given actor name
actor_name=input("Enter the actor name: ")
query=c.execute("SELECT NAME,ACTOR,ACTRESS,DIRECTOR,YEAR_OF_RELEASE FROM MOVIE WHERE ACTOR=?",(actor_name,))
r=c.fetchall()
print("Movie details for Actor "+actor_name)
for j in r:
    print("***********************")
    print("Movie Name:"+j[0])
    print("Actor:"+j[1])
    print("Actress:"+j[2])
    print("Director:"+j[3])
    print("Year of release:",i[4])
    print("***********************\n\n\n")
    
con.commit()
con.close()