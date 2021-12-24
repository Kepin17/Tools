# This is Work Fucntion
import random
import datetime as dt

def work():
    while True:
      try:
        User_Name = str(input("\nEnter Your Name : "))
      except ValueError:
        print("\nError! Please Try Again!\n")
        continue
      else:
        work = ["Trader","Tailor","Miner","Web Developer","Game Developer","Admin","Teacher","Police Officer"
              ,"Mafia","Artist","Pianist","Youtuber","Food Vloger","Animator","CEO","Gamers","Lawyer","Cartel"]
        Salary = f"{random.randint(10,9999)}"
        Today = dt.date.today() 
        input_Random_Work = random.choice(work)
        input_today = Today
        output_Work = [User_Name , input_Random_Work , Salary , input_today ]

        break
    return output_Work