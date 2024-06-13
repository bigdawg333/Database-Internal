import sqlite3
conn =sqlite3.connect('fighterInfo.db')
cursor = conn.cursor()
def show_all_fighters():
    query = ('select * from fighterInfo;')
    cursor.execute(query)
    results=cursor.fetchall()
    print(results)
    conn.commit()
def show_all_striker_based_fighters():
    query = ('select * from fighterInfo where base = \"Boxing\" or base = \"Kickboxing\" or base = \"Muay Thai\";')
    cursor.execute(query)
    results=cursor.fetchall()
    print(results)
    conn.commit()
def show_all_fighters_with_30_plus_wins():
    query = ('select * from fighterInfo where wins >= 30;')
    cursor.execute(query)
    results=cursor.fetchall()
    print(results)
def show_all_fighters_with_40plus_fights():
    query = ('select * from fighterInfo where wins + losses >= 40;')
    cursor.execute(query)
    results=cursor.fetchall()
    print(results)
keepGoing = True
while keepGoing:
    print("Input the number corresponding to the query you wish to execute.")
    print("1 = show all fighters on the list in order of their IDs.")
    print("2 = show all fighters on the list with striking bases.")
    print("3 = show all fighters on the list with more than 30 wins.")
    print("4 = show all fighters on the list with more than 40 total fights.")
    option_choice = int(input(">"))
    if option_choice == 1:
        show_all_fighters()
        print("do you have further querys?(y/n)")
        response = input (">")
    elif option_choice == 2:
        show_all_striker_based_fighters()
        print("do you have further querys?(y/n)")
        response = input (">")
    elif option_choice == 3:  
           show_all_fighters_with_30_plus_wins()
           response = input (">")
    elif option_choice == 4: 
        show_all_fighters_with_40plus_fights()
        print("do you have further querys?(y/n)")
        response = input (">")
    else:
        print("This is not a valid option. Try again and be sure to input a valid choice this time.") 
    if response == "y":
        keepGoing = True
    elif response == "n":
        keepGoing = False
print("thank you for your time")
conn.close()
