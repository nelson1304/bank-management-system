import csv
class withdraw():
    def withdraw(self):
        accno = int(input("enter the accno:>"))
        with open("atm.csv", "r") as csv_file:
            r = csv.reader(csv_file)
            lines = list(r)
            amount = int(input("enter the amount to be withdraw:>"))
            for i in lines:
                if(str(accno) in str(i[1])):
                    amount=int(i[2])-amount
                    i[2]=amount
                    print("balance:>",amount)



            writer = csv.writer(open('atm.csv', 'w'))
            writer.writerows(lines)
