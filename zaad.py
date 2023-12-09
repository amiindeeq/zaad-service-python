bal = 10000

while True:
    passcode = int(input("Enter the passcode: "))

    if passcode == 8877:
        while True:
            print("1. Check Balance")
            print("2. Send Money")
            print("3. Withdraw Money")
            print("4. Deposit Money")
            print("5. Transaction History")
            print("6. E-Voucher")
            print("7. Logout")

            opt = int(input("Enter an option: "))

            if opt == 1:
                print("Your balance is: $", bal)
            elif opt == 2:
                num = input("Enter the recipient's number: ")
                mon = int(input("Enter the amount to send: "))
                print("Are you sure you want to send $", mon, " to ", num, "?")

                confirm = input("Enter 'yes' to confirm or 'no' to cancel: ")

                if confirm.lower() == "yes":
                    remaining_bal = bal - mon
                    if remaining_bal < 0:
                        print("Insufficient funds.")
                    else:
                        print("You have successfully sent $", mon, " to ", num)
                        bal = remaining_bal
                else:
                    print("Transaction canceled.")
            elif opt == 3:
                num = input("Enter your number: ")
                mon = int(input("Enter the amount to withdraw: "))
                print("Are you sure you want to withdraw $", mon, " from ", num, "?")

                confirm = input("Enter 'yes' to confirm or 'no' to cancel: ")

                if confirm.lower() == "yes":
                    remaining_bal = bal - mon
                    print("You have successfully withdrawn $", mon, " from ", num)
                    bal = remaining_bal
                else:
                    print("Transaction canceled.")
            elif opt == 4:
                num = input("Enter your number: ")
                mon = int(input("Enter the amount to deposit: "))
                print("Are you sure you want to deposit $", mon, " to ", num, "?")

                confirm = input("Enter 'yes' to confirm or 'no' to cancel: ")

                if confirm.lower() == "yes":
                    remaining_bal = bal + mon
                    print("You have successfully deposited $", mon, " to ", num)
                    bal = remaining_bal
                else:
                    print("Transaction canceled.")
            elif opt == 5:
                print("1. View Last Transaction")
                print("2. View Transaction History")
                print("3. Go Back")

                sub_opt = int(input("Enter an option: "))

                if sub_opt == 1:
                    print("Viewing last transaction...")
                elif sub_opt == 2:
                    print("Viewing transaction history...")
                elif sub_opt == 3:
                    break
            elif opt == 6:
                num = input("Enter the voucher number: ")
                mon = int(input("Enter the amount to spend: "))
                print("Are you sure you want to spend $", mon, " on voucher ", num, "?")

                confirm = input("Enter 'yes' to confirm or 'no' to cancel: ")

                if confirm.lower() == "yes":
                    remaining_bal = bal - mon
                    print("You have successfully spent $", mon, " on voucher ", num)
                    bal = remaining_bal
                else:
                    print("Transaction canceled.")
            elif opt == 7:
                print("Logging out...")
                break

        choice = input("Enter 'back' to go back to the password prompt or 'exit' to quit: ")
        if choice.lower() == "exit":
            break

    else:
        print("Invalid passcode.")

    choice = input("Enter 'back' to go back to the password prompt or 'exit' to quit: ")
    if choice.lower() == "exit":
        break