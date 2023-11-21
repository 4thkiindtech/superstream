import mysql.connector
from werkzeug.security import generate_password_hash

# Connect to the database
cnx = mysql.connector.connect(user='username', password='password',
                              host='localhost',
                              database='myDB')
cursor = cnx.cursor()

# Retrieve the input data
_form = cgi.FieldStorage()
fname = _form.getvalue('fname')
lname = _form.getvalue('lname')
email = _form.getvalue('email')
password = _form.getvalue('password')

# Hash the password
hashed_password = generate_password_hash(password)

# Insert the data into the database
query = ("INSERT INTO users (fname, lname, email, password) "
         "VALUES (%s, %s, %s, %s)")

args = (fname, lname, email, hashed_password)

cursor.execute(query, args)

# Commit the changes and close the connection
cnx.commit()
cursor.close()
cnx.close()

print("Registration successful")