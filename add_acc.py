import csv
class add_account():
    def add_account(self):
        with open("atm.csv", "a") as csv_file:
            r = csv.writer(csv_file)
            print('$$$$ ADD ACCOUNT $$$$')
            name=input("enter the  name:>")
            accno=int(input("enter the accno:>"))
            deposit_amount=int(input("enter the amount:."))
            tup1=(name,accno,deposit_amount)
            r.writerow(tup1)
            print("account added!!!")

