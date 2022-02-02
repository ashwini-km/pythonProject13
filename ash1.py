import mysql.connector
import pickle
mydb=mysql.connector.connect(user="root",
                             passwd="root",
                             host="localhost",
                             database="bank"
                             )
mycursor=mydb.cursor()#buffered=True
def Menu():
    print("*"*140)
    print("MAIN MENU".center(140))
    print("1. Insert Records".center(140))
    print("2. Display Records as per Account Number". center(140))
    print("   a. Sorted as per Account Number".center(140))
    print("   b. Sorted as per Customer Name".center(140))
    print("   c. Sorted as per Custome Balance".center(140))
    print("3. Search record details as per the account number".center(140))
    print("4. Update record".center(140))
    print("5. Delete record".center(140))
    print("6. TransactionDebit/withdraw from the account".center(140))
    print("   a. Debit/withdraw from the account".center(140))
    print("   b. Credit into the account".center(140))
    print("7. Exit".center(140))
    print("*"*140)
def MenuSort():
    print(" a. Sorted as per Account number".center(140))
    print(" b. Sorted as per Customer Name".center(140))
    print(" c. Sorted as per Customer Balance".center(140))
    print(" d. back".center(140))
def MenuTransaction():
    print(" a. Debit/withdraw from the account".center(140))
    print(" b. Credit into the account".center(140))
    print(" c. Back".center(140))
def create():
    try:
        mycursor.execute('create table bank(ACCNO varchar(10),NAME varchar(20),MOBILE varchar(10),EMAIL ADDRESS varchar(20),Country varchar(20),Bal varchar(10)')
        print("table created")
        Insert()
    except:
        print("table exist")
        Insert()
def Insert():
            while True:
             Acc=input("Enter account no")
             Name=input("Enter name")
             Mob=input("Enter mobile")
             email=input("Enter email")
             Add=input("Enter Address")
             City=input("Enter City")
             Country=input("Enter country")
             Bal=input("Enter Balance")
             Rec=[Acc,Name.upper(),Mob,email.upper(),Add.upper(),City.upper(),Country.upper(),Bal]
             Cmd="insert into BANK values(%s,%s,%s,%s,%s,%s,%s,%s)"
             mycursor.execute(Cmd,Rec)
             mycursor.fetchall()
             mydb.commit()
             ch=input("Do u want to more records")
             if ch=='N' or ch=='n':
               break
def DispSortAcc():
    try:
        cmd="select * from BANK order by ACCNO"
        mycursor.execute(cmd)
        F="%15s  %15s  %15s  %15s  %15s  %15s  %15s  %15s"
        print(F % ("ACCNO","NAME", "MOBILE", "EMAIL ADDRESS","COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("="*125)
        for i in mycursor:
            for j in i:
                print("%14s" % j, end=" ")
            print()
        print("="*125)
    except():
        print("Table doesn't exist")
def DispSortBal():
    try:
        cmd="select * from BANK order by BALANCE"
        mycursor.execute(cmd)
        F = "%15s  %15s  %15s  %15s  %15s  %15s  %15s  %15s"
        print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
        print("=" * 125)
        for i in mycursor:
            for j in i:
                print("14s" % j, end=" ")
            print()
        print("="*125)
    except:
        print("Table doesn't exist")
def DispSearchAcc():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        ch=input("Enter the accountno to be searched")
        for i in mycursor:
            if i[0]==ch:
                print("="*125)
                F="%15s  %15s  %15s  %15s  %15s  %15s  %15s  %15s"
                print(F % ("ACCNO", "NAME", "MOBILE", "EMAIL ADDRESS", "COMPLETE ADDRESS", "CITY", "COUNTRY", "BALANCE"))
                print("=" * 125)

                for j in i:
                  print("14s" % j, end=" ")
                print()
                break
            else:
             print("Record not found")
    except:
        print("Table doesn't exist")
def update():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        A=input("Enter the account no whose details to be changed")
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                ch=input("change Name(Y/N)")
                if ch=='y' or ch=='Y':
                    i[1]=input("Enter Name")
                    i[1]=i[1].upper()
                ch=input("change Mobile(Y/N)")
                if ch=='y' or ch=='Y':
                    i[2]=input("Enter Mobile")
                ch=input("Change Email(Y/N)")
                if ch=='y' or ch=='Y':
                    i[3]=input("Enter email")
                    i[3]=i[3].upper()
                ch = input("Change Address(Y/N)")
                if ch=='y' or ch=='Y':
                    i[4]=input("Enter Address")
                    i[4]=i[4].upper()
                ch = input("Change City(Y/N)")
                if ch=='y' or ch=='Y':
                    i[5] = input("Enter City")
                    i[5] = i[5].upper()
                ch = input("Change Country(Y/N)")
                if ch == 'y' or ch=='Y':
                   i[6] = input("Enter Country")
                   i[6] = i[6].upper()
                ch=input("Change Balance(Y/N)")
                if ch=='y' or ch=='Y':
                    i[7]=float(input("Enter Balance"))
                cmd="UPDATE BANK SET NAME=%s, MOBILE=%s, EMAIL=%s, ADDRESS=%s, CITY=%S, COUNTRY=%s, BALANCE=%s, WHERE ACCNO=%s"
                val=(i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Updated")
                break
            else:
                print("Record not found")
    except:
        print("No such table")
def Delete():
    try:
        cmd="select * from BANK"
        mycursor.execute(cmd)
        A=input("Enter the account no whose details to be changed")
        for i in mycursor:
            i=list(i)
            if i[0]==A:
                cmd="delete from bank where accno=%s"
                val=(i[0],)
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Account Deleted")
                break
        else:
            print("Record not found")
    except:
        print("No such table")

def debit():
    cmd = "select * from BANK"
    mycursor.execute(cmd)
    print("Please note that the money can only be debited if min balance of Rs 5000 exists")
    acc=input("Enter the account no from which the money is to be debited")
    for i in mycursor:
        i = list(i)
        if i[0]==acc:
            Amt=float(input("Enter the amount to be withdrawn"))
            if i[7]-Amt>=5000:
                i[7]-=Amt
                cmd="UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
                val=(i[7],i[0])
                mycursor.execute(cmd,val)
                mydb.commit()
                print("Amount Debited")
                break
            else:
                print("There must be min balance of Rs 5000")
def credit():
    try:
     cmd = "select * from BANK"
     mycursor.execute(cmd)
     S=mycursor.fetchall()
     print("Please note that the money can only be debited if min balance of Rs 5000 exists")
     acc = input("Enter the account no from which the money is to be debited")
     for i in S:
        i = list(i)
        if i[0] == acc:
            Amt = float(input("Enter the amount to be withdrawn"))

            i[7] += Amt
            cmd = "UPDATE BANK SET BALANCE=%s WHERE ACCNO=%s"
            val = (i[7], i[0])
            mycursor.execute(cmd, val)
            mydb.commit()
            print("Amount Credited")
            break
        else:
         print("Record not found")

    except:
     print("Table doesn't exist")
while True:
    Menu()
    ch=input("Enter your choice:")
    if ch=="1":
     Create()
    elif ch=="2":
        while True:
         MenuSort()
         ch1=input("Enter choice a/b/c/d")
         if ch1 in ['a', 'A']:
          DispSortAcc()
         elif ch1 in ['b', 'B']:
          DispSortName()
         elif ch1 in ['c', 'C']:
          DispSortBal()
         elif ch1 in ['d', 'D']:
                print("Back to the main menu")
                break
         else:
                print("invalid choice")
    elif ch=="3":
     DispSearchAcc()
    elif ch=="4":
     update()
    elif ch=="5":
     Delete()
    elif ch=="6":
     while True:
         MenuTransaction()
         ch1=input("Enter choice a/b/c")
         if ch1 in ['a','A']:
          debit()
         elif ch1 in ['b','B']:
          credit()
         elif ch1 in ['c','C']:
          print("Back to the main menu")
          break
         else:
          print("Invalid choice")
    elif ch=="7":
      print("Exiting...")
      break
    else:
      print("Wrong choice Entered")




















