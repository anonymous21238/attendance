import sqlite3
import importlib

def option1():
    print("Option 1 selected")
    import scanner
    importlib.reload(scanner)


def option2():
    print("Option 2 selected")
    import attHistory
    importlib.reload(attHistory)

def option3():
    # password = 123
    password = input("Enter the password")
    if(password == '123'):
        print("Option 3 selected")
        print("1. Make more QR codes")
        print("2. Make new Database")
        n = int(input("Enter your choice: "))
        if(n == 1):
            import qrGEN
            importlib.reload(qrGEN)
        if(n == 2):
            import dbMaking
            importlib.reload(dbMaking)
        else:
            print("No such option exists")
    else:
        print("Wrong Password")

    

def main():
    while True:
        print("\nMenu:")
        print("1. Scan your QR code")
        print("2. Know about your Attendance History")
        print("3. Only authorised entry (database)")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()



































































































































# conn = sqlite3.connect('Database\\attendance.db')







# command = "select * from attendance"
# result = conn.execute(command)
# print(result)
# for i in result:
#     print(i)