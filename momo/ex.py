def send_money():
    phone = input("Enter receipients number: ")

    if len(phone) != 10:
        print("Invalid phone number")
        return

    try:
        money = int(input("Enter money to send: "))
        pin = int(input("Enter pin: "))
    except:
        print("Money and PIN must be numbers")
        return

    if pin != 2008:
        print("Wrong PIN")
    else:
        # delay()
        print(f"Money sent to {phone}")

send_money()