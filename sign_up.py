from email_verify import Email_verify
from sqliteHelper import Sqlite
from Face_Recognise import Face_Recognize
import uuid
import os

class Sign_up():
    def sign_up(self,user_name,email):
        # 1) Functions variables
        ob=Sqlite()
        #ob.sql_table()
        x=Email_verify()
        face=Face_Recognize()
        
        print("username is ",user_name)
        # 2) User name verification
        #user_name=input("User_Id")
        y=ob.check_user(user_name)
        # while y!=1:
        if y==0:
            print("Username Already exists")
            return "Username Already Exists"
        #         user_name=input("User_Id")
        #         y=ob.check_user(user_name)
                

        # 3) Email Id Verification
        #email=input("Email_Id")
        t=x.verify_email(email)
        if t==-1:
            return "Invalid Formate of Email"
            print("Invalid formate")
        elif t==0:
            return "Email doesn't exists"
            print("Email doesn't exists")
            email=input("Email_Id")
            t=x.verify_email(email)
            
        # 4) Face_Recognition Verification
        return "Taking photos"
        data_path='E:/python projects/python face recognition/user_photo/'
        os.mkdir(data_path+user_name)
        print("Directory is formed")
        u=face.Signup(user_name)

        if u==1:
            user_id=str(uuid.uuid4())
            li=[]
            li.append(user_id)
            li.append(user_name)
            li.append(email)
            ob.insert_user(li)
            return user_name
            print("Signed up Successfully")
        else:
            return ""