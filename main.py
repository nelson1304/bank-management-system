import balance
import deposit
import login
import remove_acc
import withdraw
import add_acc
import all_account
class main():
    print("$$$$$ Bank Management System $$$$$")
    a = login.login()
    b =deposit.deposit()
    c =balance.check_balance()
    d =withdraw.withdraw()
    e =add_acc.add_account()
    f=remove_acc.remove_acc()
    g=all_account.all_account()


    while (1):
        print("$$$$LOGIN WINDOW$$$$")
        print("1.login 2.set password")
        a1 = int(input("enter your choice:>"))

        if (a1 == 1):
            a.login1()
            break
        if (a1 == 2):
            a.setpassword()
            continue
        else:
            print("try again")

    while(1):
        print("*****************")
        print("1.deposit amount")
        print("2.check balance")
        print("3.withdraw amount")
        print("4.add account")
        print("5.remove account")
        print("6.all account details")
        print("7.exit")
        print("******************")

        a2=int(input("enter the option:>"))
        if(a2==1):
            b.deposit()
            continue
        if(a2==2):
            c.check_balance()
            continue
        if(a2==3):
            d.withdraw()
            continue
        if(a2==4):
            e.add_account()
            continue
        if(a2==5):
            f.remove_acc()
            continue
        if(a2==6):
            g.all_account()
            continue
        if(a2==7):
            quit()
        else:
            print("try again")