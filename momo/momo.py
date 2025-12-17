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
        phone = str(input("Enter phone number: "))
        for dot in range(5):
            print(".")
            time.sleep(1)
        print(f"money sent to {phone}")

def send_money():
    try: 
        phone = str(input("Enter receipients number: "))
        if len(phone) != 10:
            print("Invalid phone number")
            return
        else:
            try:
                money = int(input("Enter money to send: "))
                pin = int(input("Enter pin: "))
                if pin != 2008:
                    print("Wrong PIN")
                else:
                    delay()
                    print(f"Monet sent to {phone}")
            except:
                print("PIN must be numbers")
    
    except:
        print("Receipient number must be integer")

def coffe():
    try:    
        amount = int(input("Enter amount: "))
        if amount > 0:
            print("Thanks for coffe!!")
        else:
            print("Invalid amount")
    except:
        print("Money should be numbers")

def exit():
    print("Exiting", end="", flush=True)
    for i in range(5):
        print(".",end="",flush=True)
        time.sleep(0.5)
    print("\nThanks for visitting")
    
while True:
    main_menu()

    try:
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
            break
    except:
        print("Choice must be a number")
        