import sqlite3
conn =sqlite3.connect('fighterInfo.db')
cursor = conn.cursor()
keepGoing = True
while keepGoing:
    print("What is your query?(no need for speech marks.)")
    query = input(">")
    cursor.execute(query)
    results=cursor.fetchall()
    print(results)
    conn.commit()
    print("do you have further querys?(y/n)")
    response = input (">")
    if response == "y":
        keepGoing = True
    elif response == "n":
        keepGoing = False
print("thank you for your time")
conn.close()
