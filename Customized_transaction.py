from sqliteHelper import Sqlite
from sqlite_transaction import Sqlite_trans
from particular_transactions import Particular_transactions

#Functions

class Customized_transaction():
    def __init__(self):
        self.sq=Sqlite()
        self.sq_trans=Sqlite_trans()
        self.parti_trans=Particular_transactions()

    def customized_transaction(self,user_name):
        di=self.sq_trans.customized_transaction(self.sq.find_id_by_username(user_name))
        print("User Name         Total Amount             Amount")
        for i in di.keys():
            print(self.sq.find_username_by_id(i),"                 ",di[i]['Amount'],"                 ",di[i]['Amount_owe'])
            inp=input("1.View all transactions 2.Settle up 3.continue")
            if inp=="1":
                self.parti_trans.particular_transactions(self.sq.find_id_by_username(user_name),i)
            if inp=="2":
                self.sq_trans.settle_up(self.sq.find_id_by_username(user_name),i)
            

