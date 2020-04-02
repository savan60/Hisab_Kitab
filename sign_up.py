from email_verify import Email_verify
from sqliteHelper import Sqlite
from Face_Recognise import Face_Recognize
import uuid
import os
class Sign_up():
    def __init__(self):
        # 1) Functions variables
        ob=Sqlite()
        #ob.sql_table()
        x=Email_verify()
        face=Face_Recognize()

        # 2) User name verification
        user_name=input("User_Id")
        y=ob.check_user(user_name)
        while y!=1:
            if y==0:
                print("Username Already exists")
                user_name=input("User_Id")
                y=ob.check_user(user_name)

        # 3) Email Id Verification
        email=input("Email_Id")
        t=x.verify_email(email)
        while t!=1:
            if t==-1:
                print("Invalid formate")
            else:
                print("Email doesn't exists")
                email=input("Email_Id")
                t=x.verify_email(email)
            
        # 4) Face_Recognition Verification
        data_path='E:/python projects/python face recognition/user_photo'
        os.mkdir(data_path+user_name)
        u=face.Signup(user_name)

        if u==1:
            user_id=str(uuid.uuid4())
            li=[]
            li.append(user_id)
            li.append(user_name)
            li.append(email)
            ob.insert_user(li)
            print("Signed up Successfully")