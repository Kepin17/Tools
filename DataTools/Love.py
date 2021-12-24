
import random
import datetime as dt

# This is Love Fucntion

def love():
    while True:
      try:
        name = str(input("\nEnter User 1 Name : "))
        user_name2 = str(input("Enter User 2 Name : "))
      except ValueError:
        print("\nError! Please Try Again!\n")
        continue
      else:
      
        input_Random_persen_Love = ["0% = Waduhh!! Kurang cocok Kamu","25% = Sepertinya ada sedikit perbedaan,Semangat Gan!",
                                  "50% = Wah Keren Kamu!","75% = Kalian Pasangan yang serasi ya","100% = Wah Ditunggu ya undanganya! "]       
        input_name = name 
        input_user_2 = user_name2 
        result = random.choice(input_Random_persen_Love)
        output = [input_name , input_user_2 , result]
        break
    return output

