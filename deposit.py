import csv
class deposit():
    def deposit(self):
        print("$$$$ DEPOSIT $$$$")
        accno=int(input("enter the acc no:>"))
        with open("atm.csv", "r") as csv_file:
            r = csv.reader(csv_file)
            lines=list(r)
            amount=int(input("enter the amount to be deposited:>"))
            for i in lines:
                if(str(accno) in str(i[1])):
                    print("customer name:>",i[0])
                    amount+=int(i[2])
                    i[2]=amount
                    print("balance:>",amount)
            writer = csv.writer(open('atm.csv', 'w'))
            writer.writerows(lines)

