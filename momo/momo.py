import time

def delay():
    print("Processing", end="", flush=True)
    for i in range(5):
        print(".", end="", flush=True)
        time.sleep(1)

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

    elif choice == 2:
        phone = str(input("Enrter phone number: "))
        for dot in range(5):
            print(".")
            time.sleep(1)
        print(f"money sent to {phone}")

def send_money():
    phone = str(input("Enter receipients number: "))
    if len(phone) != 10:
        print("Invalid phone number")
        return
    else:
        money = int(input("Enter money to send: "))
        pin = int(input("Enter pin: "))
        if pin != 2008:
            print("Wrong PIN")
        else:
            delay()
            print(f"Monet sent to {phone}")

def coffe():
    amount = int(input("Enter amount: "))
    if amount > 0:
        print("Thanks for coffe!!")
    else:
        print("Invalid amount")

def exit():
    print("Exiting...") 
    time.sleep(2)   
    print("Goodbye!")
    return


while True:
    main_menu()

    choice = int(input("Your choice: "))

    if choice == 1:
        print("Air time purchasing")
        airtime()

    elif choice == 2:
        send_money()

    elif choice == 3:
        coffe()

    elif choice == 4:
        exit()
        