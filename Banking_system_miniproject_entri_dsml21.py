


def Abid():
    balance=100000
    print("your Balance is:",balance)
    W=input("Press W for the withdrawal \nPress D for deposit:")
    if W=="W":
        A=int(input("Enter the Amount:"))
        balance=balance-A
        print("Your Balance Is:",balance)
    elif W=="D":
        A=int(input("Enter The Amount:"))
        balance=balance+A
        print("Your Balance Is:",balance)


def Shuhaib():
    balance=15000
    print("Your Balance Is:",balance)
    W=input("Press W for the withdrawal \npress D for deposit:")
    if W=="W":
        A=int(input("Enter The Amount:"))
        balance=balance-A
        print("Your Balance Is:",balance)
    elif W=="D":
        A=int(input("Enter The Amount:"))
        balance=balance+A
        print("Your Balance Is:",balance)



def Haris():
    balance=75000
    print("Your Balance is",balance)
    W=input("Press W for the withdrawal \n press D for deposit")
    if W=="W":
        A=int(input("Enter The Amount:"))
        balance=balance-A
        print("Your Balance Is:",balance)
    elif W=="D":
        A=int(input("Enter The Amount:"))
        balance=balance+A
        print("Your Balance is:",balance)



names={"Abid":1234,"Shuhaib":5678,"Haris":9010}
username=input("Enter your Username:")
if username in names.keys():
    pas=int(input("Enter your Password:"))
    if pas==1234:
        Abid()
    elif pas==5678:
        Shuhaib()
    elif pas==9010:
        Haris()
    else:
        print("wrong password")
else:
    print("wrong password")
