#ATM APPLICATION:
card=input("Insert the card:")
password=1234
acc_bal=100000
if card=="c":
    print("Welcome Pooja")
    while True:
        if password==1234:
            print('''Choose the following Options:
                                1.Balance Enquiry
                                2.Withdraw''')
            a=int(input("option:"))
            if a==2:
                r=int(input("Enter amount:"))
                acc_bal=acc_bal-r
                print("Remaining Balance after Transaction is:",acc_bal)
            elif a==1:
                print(acc_bal)
            else:
                print("invalid option")
        else:
            print("Incorrect Password")
    else:
        print("Invalid user:")        
