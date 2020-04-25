import csv
class remove_acc():
    def remove_acc(self):
        with open("atm.csv", "r") as csv_file:
            r = csv.reader(csv_file)
            lines=list(r)
            accno=int(input("enter the  accno:>"))
            for i in lines:
              if(str(accno) in str(i[1])):
                   lines.remove(i)
                   print("account removed successfully!!")
            writer = csv.writer(open('atm.csv', 'w'))
            writer.writerows(lines)

