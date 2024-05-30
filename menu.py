from module import bank

bank = bank()

serv = int(input("Service Provided:\n1.Acc Cretion\n2.Deposit\n3.Withdraw\n4.Fixed Deposit\n5.Exit\n"))
print(bank.data)


if serv == 1:
    name = input("Enter Name: ")
    bal = input("Enter Deposit Amt: ")
    fd = input("Enter FD Amt: ")
    bank.create(name,bal,fd)
    bank.create()
elif serv == 2:
    accno =input("Enter Accno: ")
    depamt =input("Enter Deposit Amount: ")
    bank.deposit(accno,depamt)
elif serv == 3:
    accno =input("Enter Accno: ")
    witamt =input("Enter Withdraw Amount: ")
    bank.withdraw(accno,witamt)
elif serv == 4:
    accno =input("Enter Accno: ")
    fdamt =input("Enter FD Amount: ")
    yrs = input("Enter FD Years: ")
    bank.fd(accno,fdamt,yrs)
elif serv == 5:
    print("Thank You!!!")