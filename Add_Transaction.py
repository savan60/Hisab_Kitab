from sqliteHelper import Sqlite
from sqlite_transaction import Sqlite_trans
from Send_mail import Send_Email
import uuid
import datetime

class Add_transaction():
    def __init__(self):
        self.sq = Sqlite()
        self.mail=Send_Email()
        self.sq_trans = Sqlite_trans()

    def add_transaction(self,user_name):
        transaction_to = input("Name of person to add transaction")
        if self.sq.find_if_username_exist(transaction_to):
            print("User found")
            amount = int(input("Amount to be paid"))
            description = input("description of transaction")
            transaction_type = input("1.Equally distributed 2.Fully owned")
            amount_owe = -1
            lis = []
            if transaction_type == "1" or transaction_type == "2":
                trans_id = str(uuid.uuid4())
                if transaction_type=="1":
                    amount_owe=amount/2
                else:
                    amount_owe=amount
                lis=(trans_id,self.sq.find_id_by_username(user_name),self.sq.find_id_by_username(transaction_to),amount,amount_owe,description, datetime.datetime.now(),'N')
                self.sq_trans.insert_transaction(lis)
                print("Transaction Completed")
#                 message="From: "+ user_name+""" <from@fromdomain.com> To: """ + transaction_to+ """<to@todomain.com>
# Subject: """+description + "Total Amount : "+ str(amount) +" Amount to pay:"+str(amount_owe)
#                 #message="From: "+user_name+" To: "+transaction_to+"\ndescription: "+description+"\nTotal amount: "+str(amount)+"\nAmount to pay: "+str(amount_owe)
#                 self.mail.send_mail(self.sq.find_email_by_username(transaction_to),user_name,message)
#                 print("Message sent")
            else:
                print("Invalid input")
        else:
            print("No such user Found!")
