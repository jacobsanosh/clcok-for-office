from time import ctime
from gtts import gTTS
from datetime import datetime
from playsound import playsound


print("this clock is mainly for office purpose from 9 to 6")
print("--------------------------------------")
try :
    w_duration,e_duration,p_duration=map(int,input("enter by order water duration,eye rest duration,physical duration").split())

except ValueError:
    print("please enter the value one by one ")

#taking current min hour and min for checking the time limit of office
c_time_hour,c_time_min=map(int,datetime.now().strftime("%I %M").split())
ap=datetime.now().strftime("%p") #here ap is ussed to find am or pm


try:
    yes=True
    while True:
        #to set the time limit
        if (c_time_hour>=9 and ap=="AM") or (c_time_hour<=5 and ap=="PM"):
        
            # taking the current time
            r_time_min,r_time_sec=map(int,datetime.now().strftime("%M %S").split())
            if r_time_min<c_time_min: # if it is less than example r_time=5 and c_time is 55 then adding with 60
                r_time_min+=60
            diff=r_time_min-c_time_min #finding the differnece 
            print(r_time_sec)

            #checking the time whether they are qual ti specified duration
            if c_time_min%w_duration==r_time_min%w_duration and diff%w_duration==0 and diff!=0 and r_time_sec==0: 
                while yes:
                    print("please drik some water")
                    #for converting the text to audio
                    obj = gTTS(text="please drink some water ", lang='en', slow=False)  
                    obj.save("drink.mp3")
                    playsound("drink.mp3")
                    check_op=input("have u drik it")
                    if check_op.upper()=="YES":
                        yes=False
                else:
                    yes=True
                
                
                #same as here

            if c_time_min%e_duration==r_time_min%e_duration and diff%e_duration==0 and diff!=0 and r_time_sec==0:
                yes=True
                while yes:
                    print("please do some eye exercise")
                    obj = gTTS(text="please do some eye exercise ", lang='en', slow=False)  
                    obj.save("eye.mp3")
                    playsound("eye.mp3")
                    check_op=input("have u did eye exercise it")
                    if check_op.upper()=="YES":
                        yes=False
                else:
                    yes=True
                
            #same
            if c_time_min%p_duration==r_time_min%p_duration and diff%p_duration==0  and diff!=0 and r_time_sec==0:
                yes=True
                while yes:
                    print("please do some physical exercise")
                    obj = gTTS(text="please do some physical exercise ", lang='en', slow=False)  
                    obj.save("physique.mp3")
                    playsound("physique.mp3")
                    check_op=input("have u did physical exercise it")
                    if check_op.upper()=="YES":
                        yes=False
                else:
                    yes=True
            #for  after checking time 
            else:
                c_time_hour=int(datetime.now().strftime("%I"))
                continue
            
        else:
            print("today is completed")

except NameError:
    print("something went wrong on the given input")
