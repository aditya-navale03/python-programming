import psycopg2

try:
    # Establish the connection
    con = psycopg2.connect(
        dbname="mysql",
        user="postgres",
        password="Ams@adi2",
        host="localhost",
        port="5432"  # Default is 5432
    )

    # Create a cursor object
    cur = con.cursor()

    #write query of create table students
    cur.query= (
        """create table students(name varhar, rollno int primary )"""
    )

    # Execute a simple query
    cur.execute()

except (Exception, psycopg2.Error) as error:
    print("Error connecting to database:", error)


    # Close the connection
finally:
    if con:
     cur.close()
     con.close()
     print("PostgreSQL connection is closed")