from sqliteHelper import Sqlite
from Face_Recognise import Face_Recognize


class Log_in():
    def log_in(self):
        user_name=input("User_name")
        ob=Sqlite()
        o=Face_Recognize()
        x=ob.check_user(user_name)
        if x==0:
            print("Correct Username")
            t=int(input("1.Face Recognition "))
            if t==1:
                o.login(user_name)
                return 1
        return 0
