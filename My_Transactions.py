from sqlite_transaction import Sqlite_trans
from sqliteHelper import Sqlite
import datetime
import pandas as pd

class My_transactions():
    def __init__(self):
        self.sq_trans=Sqlite_trans()
        self.sq=Sqlite()
    def my_trans(self,user_id):
        list_trans=self.sq_trans.my_transactions(user_id)
        for i in list_trans:
            print(self.sq.find_username_by_id(i[1]),"----->" ,self.sq.find_username_by_id(i[2]))
            print("Total Amount: ",i[3])
            print("Amount: ",i[4])
            print("Detail: ",i[5])
            dat=pd.to_datetime(i[6])
            print(dat)
            c=datetime.datetime.now()-dat
            d=str(c.days)
            if(d=='0'):
                print("today")
            else:
                print(d," before")
            if i[7]=='N':
                print("Incomplete")
            print("\n\n")