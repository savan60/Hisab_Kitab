import cv2
import numpy as np
from os import listdir
from os.path import isfile,join
import os

class Face_Recognize():
    def __init__(self):
        #self.data_path='E:/python projects/python face recognition/'
        self.face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    def face_extractor(self,img):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.face_cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5)
        
        if faces is():
            return None

        for(x,y,w,h) in faces:
            cropped_face=img[y:y+h,x:x+w]

        return cropped_face

    def face_detection(self,img,size=0.5):
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=self.face_cascade.detectMultiScale(gray,1.3,5)

        if faces is():
            return img,[]

        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
            roi=img[y:y+h,x:x+w]
            roi=cv2.resize(roi,(200,200))

        return img,roi

    def Signup(self,user_name):
        cap=cv2.VideoCapture(0)
        count=0
        while True:
            ret,frame=cap.read()
            if self.face_extractor(frame) is not None:
                count+=1
                face=cv2.resize(self.face_extractor(frame),(200,200))
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)

                file_name_path='E:/python projects/python face recognition/user_photo/'+user_name+'/user'+str(count)+'.jpg'
                cv2.imwrite(file_name_path,face)

                cv2.putText(face,str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,250,0),2)
                cv2.imshow('Face Cropper',face)
            else:
                print("Face not Found")
                pass
            if cv2.waitKey(1)==13 or count==100:
                break
            print("Count is ",count)
        cap.release()
        cv2.destroyAllWindows()
        print("done")
        return 1

    def login(self,user_name):
        data_path='E:/python projects/python face recognition/user_photo/'+user_name+"/"
        onlyfiles=[f for f in listdir(data_path) if isfile(join(data_path,f))]

        Training_Data,Labels=[],[]

        for i, files in enumerate(onlyfiles):
            image_path=data_path+onlyfiles[i]
            images=cv2.imread(image_path,cv2.IMREAD_GRAYSCALE)
            Training_Data.append(np.asarray(images,dtype=np.uint8))
            Labels.append(i)


        Labels=np.asarray(Labels,dtype=np.int32)

        model=cv2.face.LBPHFaceRecognizer_create()

        model.train(np.asarray(Training_Data),np.asarray(Labels))


        face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        cap=cv2.VideoCapture(0)
        flag=0
        while True:
            ret,frame=cap.read()

            image,face=self.face_detection(frame)

            try:
                face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                result=model.predict(face)

                if result[1]<500:
                    confidence= int(100*(1-(result[1])/300))
                    display_string=str(confidence)+"% confidence it is user"
                cv2.putText(image,display_string,(100,120),cv2.FONT_HERSHEY_COMPLEX,1,(250,120,255),2)

                if confidence>75:
                    cv2.putText(image,"Unlocked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                    break
                    cv2.imshow("Face Cropper",image)
                    
                else:
                    cv2.putText(image,"Locked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                    cv2.imshow("Face Cropper",image)
                    
            except:
                cv2.putText(image,"File Not Found",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255),2)
                cv2.imshow("Face Cropper",image)
                pass

            if cv2.waitKey(1)==13:
                break
        cap.release()
        cv2.destroyAllWindows()

# print("Welcome to Hisab Kitab")
# while(True):
#     input_user=int(input("1.Login 2.SignUp"))
#     flag=0
#     user_name=input("Username")
#     for f in listdir(data_path):
#         if f==user_name:
#             print("User already present")
#             flag=-1
#     if input_user==1:
#         face_recognize=int(input("1.Face Recognization 2.No"))
#         if face_recognize==1:
#             if flag==0:
#                 print("No user name found, try signingup")
#             else:
#                 login()
#                 print("Loged in")
#     elif input_user==2:
#         if flag==0:
#             Signup()
#             print("Signed in")
#         else:
#             print("User name is already present, try another name")
