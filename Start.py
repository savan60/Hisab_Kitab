from login import Log_in
from sign_up import Sign_up
from sqliteHelper import Sqlite
from Add_Transaction import Add_transaction
from My_Transactions import My_transactions
from Customized_transaction import Customized_transaction

print("Welcome to Hisab_Kitab")
inp=int(input("1. Login 2. Sign up"))

#Functions
log=Log_in()
sq=Sqlite()
sign=Sign_up()
add_trans=Add_transaction()
customized=Customized_transaction()

username=""
my_tran=My_transactions()
flag=-1

if inp==1:
    loged_in=log.log_in()
    if loged_in!="":
        user_id=sq.find_id_by_username(loged_in)
        print("Welcome , ",loged_in)
        flag=1
        username=loged_in
    else:
        print("Try again")
        
elif inp==2:
    signed_in=sign.sign_up()
    if signed_in!="":
        user_id=sq.find_id_by_username(signed_in)
        print("Welcome ,",signed_in)
        flag=1
        username=signed_in
    else:
        print("Try again")

b=True
while(b):
    inp=int(input("1.Add Transaction 2.Customized Transactions 3.My Transactions 4.Settle up"))
    if inp==1:
        add_trans.add_transaction(username)
    elif inp==2:
        customized.customized_transaction(username)
    elif inp==3:
        my_tran.my_trans(sq.find_id_by_username(username))
    elif inp==99:
        b=False    
