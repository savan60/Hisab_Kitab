import sqlite3
import datetime
from sqlite3 import Error


class Sqlite_trans():
    def __init__(self):
        try:
            self.con = sqlite3.connect('mydatabase.db')
        except Error:
            print(Error)

    def sql_table(self):

        cursorObj = self.con.cursor()

        cursorObj.execute(
            "CREATE TABLE transactions_detail(t_id text PRIMARY KEY, from_p_id text,to_p_id text,total_amount real,amount_owe real,description_trans text,date_trans datetime,status_tran char)")

        self.con.commit()

    def insert_transaction(self, entities):
        cursorObj = self.con.cursor()

        cursorObj.execute(
            "INSERT INTO transactions_detail(t_id, from_p_id ,to_p_id,total_amount,amount_owe,description_trans,date_trans,status_tran) VALUES(?, ?, ?,?,?,?,?,?)", entities)

        self.con.commit()


# sq = Sqlite_trans()
# sq.sql_table()
# ent=("567","2344","4567",5500,"it's trial",datetime.datetime.now(),"F")
# sq.insert_user(ent)
