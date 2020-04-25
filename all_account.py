import csv
class all_account():
     def all_account(self):

        with open("atm.csv","r") as csv_file:
          r=csv.reader(csv_file)
          lines=list(r)
          for i in lines:
              print("details of", i[0],  "account")
              print(i)

