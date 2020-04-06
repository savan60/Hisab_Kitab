from sqliteHelper import Sqlite
from sqlite_transaction import Sqlite_trans
#Functions

class Customized_transaction():
    def __init__(self):
        sq=Sqlite()
        sq_trans=Sqlite_trans()
    def customized_transaction(self,user_name):
        user_name=input("Your name")
        di=self.sq_trans.customized_transaction(self.sq.find_id_by_username(user_name))
        print("User Name         Total Amount             Amount")
        for i in di.keys():
            print(self.sq.find_username_by_id(i),"                 ",di[i]['Amount'],"                 ",di[i]['Amount_owe'])

