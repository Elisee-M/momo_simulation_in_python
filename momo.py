def main_menu():
    print("1. Airtime")
    print("2. Send money")
    print("3. buy me a coffee")
    print("4. Exit")

def airtime():
    print("1. for me")
    print("2. For others")

    choice = int(input("Choice: "))
    if choice == 1:
        money = int(input("Enter money (Amount): "))
        if money > 0:
            print("Done airtime is bought sucessfully!")
        elif money <= 0:
            print("please enter valid amount!!")

main_menu()

choice = int(input("Your choice: "))

if choice == 1:
    print("Air time purchasing")
    airtime()