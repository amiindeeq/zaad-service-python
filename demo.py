bal = 10000

while True:
    passcode = int(input("Enter the passcode: "))

    if passcode == 8877:
        print("1. Itus hadhaaga")
        print("2. Lacag Dirid")
        print("3. Lacag la bixid")
        print("4. Ku iibso")
        print("5. Itus dhaqdhaqaaq")
        print("6. E-Voucher")
        print("7. Maarayn Guud")
        print("8. Ka bax")

        opt = int(input("Enter an option: "))

        if opt == 1:
            print(bal)
        elif opt == 2:
            num = input("Enter the number you want to send: ")
            mon = int(input("Enter the amount you want to send: "))
            print("Ma hubta inaad udirayso $", mon, " lambarka ", num)

            confirm = int(input("1. Haa\n2. Maya\n"))

            if confirm == 1:
                remaining_bal = bal - mon
                if remaining_bal < 0:
                    print("The money is not enough.")
                else:
                    print("Waxa udirtay $", mon, " lambarka ", num, " hadhagu waa:", remaining_bal)
            else:
                print("Macasaalama")
        elif opt == 3:
            num = input("Enter the number for the amount you want to withdraw: ")
            mon = int(input("Enter the amount you want to withdraw: "))
            print("Ma hubta inaad la baxaysid $", mon, " lambarka ", num)

            confirm = int(input("1. Haa\n2. Maya\n"))

            if confirm == 1:
                remaining_bal = bal - mon
                print("Waxa kala baxday $", mon, " lambarka ", num, " hadhagaagu waa $", remaining_bal)
            else:
                print("Macasaalama")
        elif opt == 4:
            num = input("Enter the number for the amount you want to deposit: ")
            mon = int(input("Enter the amount you want to deposit: "))
            print("Ma hubta inaad la baxaysid $", mon, " lambarka ", num)

            confirm = int(input("1. Haa\n2. Maya\n"))

            if confirm == 1:
                remaining_bal = bal - mon
                print("Waxd ku iibsaty $", mon, " lambarka ", num, " hadhagaagu waa $", remaining_bal)
            else:
                print("Macasaalama")
        elif opt == 5:
            print("1.Itus dhaqdhaaqi igu dambeeyay")
            print("2.warbixin kooban")
            print("3.Dib u noqo")

            opt = int(input("Enter an option: "))

            if opt == 1:
                print("Gali numberka")
        elif opt == 6:
            num = input("Enter the number for the voucher you want to buy: ")
            mon = int(input("Enter the amount you want to spend: "))
            print("Ma hubta inaad ugu shubaysid $", mon, " lambarka ", num)

            confirm = int(input("1. Haa\n2. Maya\n"))

            if confirm == 1:
                remaining_bal = bal - mon
                print("Waxd ku iibsaty $", mon, " lambarka ", num, " hadhagaagu waa $", remaining_bal)
            else:
                print("Macasaalama")
        elif opt == 8:
            print("Macasalama")

        break
    else:
        print("Lambarka sirta ah waa qalad")