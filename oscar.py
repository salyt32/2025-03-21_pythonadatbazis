import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql",
  database="oscar"
)

mycursor = mydb.cursor()

DATABASE = "oscar"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")

# 2. 
mycursor.execute("SELECT ev, cim FROM film WHERE nyert = 1 ORDER BY ev;")
for sor in mycursor:
    print(f"Év: {sor[0]}, Film címe: {sor[1]}")
print("-------------")

# 3. 
mycursor.execute("SELECT ev FROM film GROUP BY ev HAVING COUNT(*) >= 10;")
for sor in mycursor:
    print(f"Év: {sor[0]}")
print("-------------")

# 4. 
mycursor.execute("SELECT cim FROM film WHERE ev BETWEEN 1939 AND 1945 AND bemutato IS NOT NULL;")
for sor in mycursor:
    print(f"Film címe: {sor[0]}")
print("-------------")


# 5.
mycursor.execute("SELECT cim FROM film WHERE nyert = 1 AND YEAR(bemutato) >= ev + 10;")
for sor in mycursor:
    print(f"Film Címe: {sor[0]}")
print("-------------")