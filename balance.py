import csv
class check_balance():
    def check_balance(self):
        accno=int(input("enter the accno:>"))
        with open("atm.csv", "r") as csv_file:
            r = csv.reader(csv_file)
            lines=list(r)
            for i in lines:
                if(str(accno) in str(i[1])):
                    print("balance",i[2])
