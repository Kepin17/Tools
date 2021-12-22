from math import e, inf, radians
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

# This is Work Fucntion
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


# Calc  

def Calc():
    while True:
      try:
       print(10*"=","Calculator","="*10)
       calc_num_1  = float(input("\nPlease enter the first number : ")) 
       operator = input("What operation do you want to use : (+,-,*,/)\nYour Choose :  ")
       calc_num_2  = float(input("Please enter the second number : "))
       
       
      except ValueError:
        print("\nError! Please Try Again!\n")
        continue
      else:
        if operator=="+":
          print(calc_num_1 , "+" ,calc_num_2)
          result = calc_num_1 + calc_num_2
          output = [result]
        elif operator=="-":
          print(calc_num_1 , "-" ,calc_num_2)
          result = calc_num_1 - calc_num_2
          output = [result]
        elif operator=="*":
          print(calc_num_1 , "x" ,calc_num_2)
          result = calc_num_1 * calc_num_2
          output = [result]
        elif operator=="/":
          print(calc_num_1 , ":" ,calc_num_2)
          result = calc_num_1 / calc_num_2
          output = [result]
        else:
            print("Invalid,Try Again!")  
        break
    return output



# Games Suit


def suit():
      
    while True:
      try:
        print("\nLet's Play Rock Sciccors and Papper\n")
        player_1 = str(input("Player 1 :\n A) Rock\n B) Sciccors\n C) Papper\n Your Choose :  "))   
                       
      except ValueError:
        print("\nError! Please Try Again!\n")
        continue
      else:
        list_p2 = ["A " , "B" , "C" , "A" , "A" , "B" , "C" , 'C' , "C" , "A" , "B"] 
        player_2 = list_p2
        hasil = random.choice(player_2)

        if player_1=="A" and hasil=="C":
          print("\nRock Vs Papper ")
          result = "Player 2 Win!"
          output = [result]  

        elif player_1=="A" and hasil=="A":
          print("\nRock Vs Rock ")
          result = "Player 1 and Player 2 draw!"
          output = [result]

        elif player_1=="A" and hasil=="B":
          print("\nRock Vs Sciccors ")
          result = "Player 1 Win!"
          output = [result]  

        elif player_1=="B" and hasil=="B":
          print("\nSciccors Vs Sciccors")
          result = "Player 1 and Player 2 draw!"
          output = [result]
          
        elif player_1=="B" and hasil=="A":
          print("\nSciccors Vs Rock ")
          result = "Player 2 Win!"
          output = [result]  

        elif player_1=="B" and hasil=="C":
          print("\nSciccors Vs Papper ")
          result = "Player 1 Win!"
          output = [result]  

        elif player_1=="C" and hasil=="C":
          print("\nPapper Vs Papper")
          result = "Player 1 and Player 2 draw!"
          output = [result]
          
        elif player_1=="C" and hasil=="A":
          print("\nPapper Vs Rock ")
          result = "Player 1 Win!"
          output = [result]  

        elif player_1=="C" and hasil=="B":
          print("\nPapper Vs Sciccors ")
          result = "Player 2 Win!"
          output = [result]  
       
        else:
            print("Invalid,Please try again!")  
        
        break
    return output
        

#  This is Temperature

def Temp():
    while True:
      try:
       
       print(10*"=","Temperature Converter","="*10)
       Temp_num_1  = float(input("\nPlease enter the first number : ")) 
       Temp = input("\nWhat Temperature do you want to use :\n- C\n- R\n- F\n- K\nYour Choose :  ")
       convert = input("\nConvert To :\n- C\n- R\n- F\n- K\nYour Choose : ")
       

      except ValueError:
        print("\nError! Please Try Again!\n")
        continue
      else:
        if Temp=="C":
          print(Temp_num_1 ,"°", Temp , "=..." , "°" , convert )

          if convert=="R":
              input_converter = (4/5) * Temp_num_1
              result = f"Result : {input_converter} °R"

          elif convert=="F":
              input_converter = (9/5) *  Temp_num_1 + 32
              result = f"Result : {input_converter} °F"

          elif convert=="K":
              input_converter = 273 + Temp_num_1
              result = f"Result : {input_converter} °K"

          else:
              break    
                  
          output = [result]

        elif Temp=="R":
          print(Temp_num_1 ,"°", Temp , "=..." , "°" , convert )
          if convert=="C":
              input_converter = (5/4) * Temp_num_1
              result = f"Result : {input_converter} °C"

          elif convert=="F":
              input_converter = (9/4) *  Temp_num_1 + 32
              result = f"Result : {input_converter} °F"

          elif convert=="K":
              input_converter = (5/4) * Temp_num_1 + 273
              result = f"Result : {input_converter} °K"

          else:
              break    
         
          output = [result]
        elif Temp=="F":
          print(Temp_num_1 ,"°", Temp , "=..." , "°" , convert )
          if convert=="C":
              input_converter = (5/9) * Temp_num_1 - 32
              result = f"Result : {input_converter} °C"

          elif convert=="R":
              input_converter = (4/9) *  Temp_num_1 - 32
              result = f"Result : {input_converter} °R"

          elif convert=="K":
              input_converter = (5/4) * Temp_num_1 + 273
              result = f"Result : {input_converter} °K"

          else:
              break    
          
          output = [result]
        elif Temp=="K":
          print(Temp_num_1 ,"°", Temp , "=..." , "°" , convert )
          if convert=="C":
              input_converter = Temp_num_1 - 273
              result = f"Result : {input_converter} °C"
  
          elif convert=="R":
              input_converter = 4 / 5 * ( Temp_num_1 - 32 )
              result = f"Result : {input_converter} °R"

          elif convert=="F":
              input_converter = (Temp_num_1 - 273.15 ) * 9/5 + 32
              result = f"Result : {input_converter} °F"
         
          else:
              break    
          output = [result]
        else:
            print("Invalid,Try Again!")  
        break
    return output

def Atm():
    while True:  
      try:
        print(10*"=","Welcome To Python Bank","="*10)
        user_lang = input("\n What languages do you want to use?\n 1) English\n 2) Indonesia\n Choose (1/2): ")
      except ValueError:
        print("Error,Please Try Again!")
        continue
      else: 

        balance = 500
        pin_random = f"{random.randint(1000,9999)}"
        if user_lang =="1":
            pin = input(f"\n Please input Your 4 digit pin ({pin_random}) :\n Enter Your Pin :  ")
            if pin == pin_random:

              print("\nWhat do you want to do?\n 1) Balance\n 2) Withdraw\n 3) Deposit\n 4) Payment\n")
              menu_choise = input("Your Choose (1/2/3/4): ")
              
              if menu_choise=="1":
                  bal = balance
                  input_bal = f" \nYour Balance : ${bal}"
                  thx = "Have a nice day :D"
                  output = [input_bal,thx]
              
              
              elif menu_choise=="2":
                  withdraw = input("How much do you want to withdraw :\n 1. $50\n 2. $75\n 3. $100\n 4.custom\n Your Choose 1/2/3/4: ")
                  if withdraw=="1":
                    input_withdraw = balance - 50
                    cash = f" \nYou withdraw $50 and your balance :  ${input_withdraw}"
                    thx = " Please take your money"
                    output = [cash,thx] 
             
                  elif withdraw=="2":      
                    input_withdraw = balance - 75
                    cash = f" \nYou withdraw $75 and your balance :  ${input_withdraw}"
                    thx = " Please take your money"
                    output = [cash,thx] 
             
                  elif withdraw=="3":      
                    input_withdraw = balance - 100
                    cash = f" \nYou withdraw $100 and your balance :  ${input_withdraw}"
                    thx = " Please take your money"
                    output = [cash,thx] 

                  elif withdraw=="4":
                    bal = balance      
                    input_nominal = float(input(" Please enter the nominal : "))
                    if input_nominal >= bal:
                      output_text = "\nSorry, you don't have enough money :( "
                      thx = " Try again later,Don't Give Up!"
                      output = [output_text,thx]

                    else:                         
                        input_withdraw = bal - input_nominal 
                        thx = " Please take your money"
                        cash = f" \nYou withdraw ${input_nominal} and your balance :  ${input_withdraw}"
                        output = [cash,thx]     

                  else:
                      print("Invalid,please try again!")     

              elif menu_choise=="3":
                  deposit = input("How much do you want to desposit :\n 1. $50\n 2. $75\n 3. $100\n 4.custom\n Your Choose 1/2/3/4: ")
                 
                  if deposit=="1":
                    input_deposit = balance + 50
                    cash = f" \nYou deposit $50 and your balance :  ${input_deposit}"
                    thx = " Have a nice Day :D"
                    output = [cash,thx] 
             
                  elif deposit=="2":      
                    input_deposit = balance + 75
                    cash = f"\n You deposit $75 and your balance :  ${input_deposit}"
                    thx = " Have a nice Day :D"
                    output = [cash,thx] 
             
                  elif deposit=="3":      
                    input_deposit = balance + 100
                    cash = f" \nYou deposit $100 and your balance :  ${input_deposit}"
                    thx = " Have a nice Day :D"
                    output = [cash,thx] 

                  elif deposit=="4":
                    bal = balance      
                    input_nominal = float(input(" Please enter the nominal : "))
                    input_deposit = balance + input_nominal 
                    thx = " Have a nice Day :D"
                    cash = f" \nYou deposit ${input_nominal} and your balance :  ${input_deposit}"
                    output = [cash,thx]  

                  else:
                    print("Invalid,Please try again!")
              
              elif menu_choise=="4":
                    balance = 500
                    today = dt.date.today()
                    payment_choise = input("\nWhat are you paying for?\n Choose the option :\n 1) Tax\n 2) Internet\n 3) Electricity\n 4) PDAM\n Your Choose :")
                   
                    if payment_choise =="1":
                        tax_nominal = f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        input_taxt_id = str(input(f"\ninput your id {id_pelanggan} : "))
                        if input_taxt_id== id_pelanggan:
                            print(f" Python Tax\n Username : Admin\n Id : {input_taxt_id}\n tax : ${tax_nominal}\n {today}")
                            answer = input("Do you want to make a payment? (yes / no)\n Your Choose : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(tax_nominal)
                                result = f" \nPeyment Success! Your Balance = ${payment_status}"
                                thx = " Have a nice Day :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nThanks for coming"   
                                thx = " Have a nice Day :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")

                    elif payment_choise =="2":
                        internet =  f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        today = dt.date.today()
                        input_username =str(input("\nYour Name : ")) 
                        input_taxt_id = str(input(f"\ninput your id ({id_pelanggan}) : "))
                      
                        if input_taxt_id == id_pelanggan:
                            print(f" Python Electric\n Username : {input_username}\n Id : {input_taxt_id}\n tax : ${internet}\n {today}")
                            answer = input("Do you want to make a payment? (yes / no)\n Your Choose : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(internet)
                                result = f" \nPeyment Success! Your Balance = ${payment_status}"
                                thx = " Have a nice Day :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nThanks for coming"   
                                thx = " Have a nice Day :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")
               
                    elif payment_choise =="3":
                        bill =  f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        today = dt.date.today()
                        input_username =str(input("\nYour Name : ")) 
                        input_taxt_id = str(input(f"\ninput your id ({id_pelanggan}) : "))
                      
                        if input_taxt_id == id_pelanggan:
                            print(f"\n Python Net\n Username : {input_username}\n Id : {input_taxt_id}\n Bill : ${bill}\n {today}")
                            answer = input("Do you want to make a payment? (yes / no)\n Your Choose : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(bill)
                                result = f" Peyment Success! Your Balance = ${payment_status}"
                                thx = " Have a nice Day :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nThanks for coming"   
                                thx = " Have a nice Day :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")
               
                    elif payment_choise =="4":
                        bill =  f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        today = dt.date.today()
                        input_username =str(input("\nYour Name : ")) 
                        input_taxt_id = str(input(f"\ninput your id ({id_pelanggan}) : "))
                      
                        if input_taxt_id == id_pelanggan:
                            print(f"Python PAM\n Username : {input_username}\n Id : {input_taxt_id}\n Bill : ${bill}\n {today}")
                            answer = input("Do you want to make a payment? (yes / no)\n Your Choose : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(bill)
                                result = f" \nPeyment Success! Your Balance = ${payment_status}"
                                thx = " Have a nice Day :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nThanks for coming"   
                                thx = " Have a nice Day :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")
              else:
                print("error") 

            else:

              print("\n pin invalid,try again!")               
              choices = input("\n Do you want to try again? yes or no\n Your Choose :")
              if choices =="yes" :
                  continue
              elif choices =="no":
                  break

              else:
                print("Invalid,Please Try Again!")  


          # Indonesia Lang

        elif user_lang =="2":
            pin = input(f"\n Silahkan masukan 4 digit pin ({pin_random}) :\n Masukan pin kamu :  ")
            if pin == pin_random:

              print("\nApa yang ingin kamu lakukan?\n 1) Melihat tabungan\n 2) Menarik Tunai\n 3) Setor Tunai\n 4) Melakukan pembayaran\n")
              menu_choise = input("Your Choose (1/2/3/4): ")
              if menu_choise=="1":
                  bal = balance
                  input_bal = f" \nSaldo Rekening kamu : ${bal}"
                  thx = "Semoga harimu menyenangkan :D"
                  output = [input_bal,thx]
              
              
              elif menu_choise=="2":
                  withdraw = input("Berapa banyak yang ingin kamu ambil :\n 1. $50\n 2. $75\n 3. $100\n 4.custom\n Pilihanmu 1/2/3/4: ")
                  if withdraw=="1":
                    input_withdraw = balance - 50
                    cash = f" \nKamu menarik $50 dan saldo kamu :  ${input_withdraw}"
                    thx = " Silahkan ambil uangmu"
                    output = [cash,thx] 
             
                  elif withdraw=="2":      
                    input_withdraw = balance - 75
                    cash = f" \nKamu menarik $75 dan saldo kamu :  ${input_withdraw}"
                    thx = " Silahkan ambil uangmu"
                    output = [cash,thx] 
             
                  elif withdraw=="3":      
                    input_withdraw = balance - 100
                    cash = f" \nKamu menarik $100 dan saldo kamu  :  ${input_withdraw}"
                    thx = " Silahkan ambil uangmu"
                    output = [cash,thx] 

                  elif withdraw=="4":
                    bal = balance      
                    input_nominal = float(input(" Silahkan masukan nominal : "))
                    if input_nominal >= bal:
                      output_text = "\nMaaf,saldo kamu tidak cukup :( "
                      thx = " Coba lagi nanti,Jangan menyerah !"
                      output = [output_text,thx]

                    else:                         
                        input_withdraw = bal - input_nominal 
                        thx = " Silahkan ambil uangmu"
                        cash = f" \nKamu mengambil ${input_nominal} dan Saldo kamu :  ${input_withdraw}"
                        output = [cash,thx]     

                  else:
                      print("Invalid,please try again!")     

              elif menu_choise=="3":
                  deposit = input("Berapa banyak yang ingin kamu tabung :\n 1. $50\n 2. $75\n 3. $100\n 4.custom\n Pilihan Kamu 1/2/3/4: ")
                 
                  if deposit=="1":
                    input_deposit = balance + 50
                    cash = f" \nKamu memasukan $50 dan saldo kamu :  ${input_deposit}"
                    thx = " Have a nice Day :D"
                    output = [cash,thx] 
             
                  elif deposit=="2":      
                    input_deposit = balance + 75
                    cash = f"\nKamu memasukan $75 dan saldo kamu :  ${input_deposit}"
                    thx = " Have a nice Day :D"
                    output = [cash,thx] 
             
                  elif deposit=="3":      
                    input_deposit = balance + 100
                    cash = f" \nKamu memasukan $100 dan saldo kamu  :  ${input_deposit}"
                    thx = " Have a nice Day :D"
                    output = [cash,thx] 

                  elif deposit=="4":
                    bal = balance      
                    input_nominal = float(input(" Silahkan masukan nominal : "))
                    input_deposit = balance + input_nominal 
                    thx = " Semoga harimu menyenangkan :D"
                    cash = f" \nKamu memeasukan ${input_nominal} dan tabungan kamu :  ${input_deposit}"
                    output = [cash,thx]  

                  else:
                    print("Invalid,Please try again!")
              
              elif menu_choise=="4":
                    balance = 500
                    today = dt.date.today()
                    payment_choise = input("\nKamu ingin membayar untuk apa?\n Silahkan pilih beberapa opsi :\n 1) Pajak\n 2) Internet\n 3) Listrik\n 4) PDAM\n Pilihan kamu :")
                   
                    if payment_choise =="1":
                        tax_nominal = f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        input_taxt_id = str(input(f"\ninput your id {id_pelanggan} : "))
                        if input_taxt_id== id_pelanggan:
                            print(f" Python Tax\n Username : Admin\n Id : {input_taxt_id}\n tax : ${tax_nominal}\n {today}")
                            answer = input("apakah kamu mau melakukan pembayaran? (yes / no)\n Pilihan kamu : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(tax_nominal)
                                result = f" \nPembayaran berhasil! Saldo kamu = ${payment_status}"
                                thx = " Have a nice Day :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nTerimakasih karena sudah berkunjung"   
                                thx = " Semoga harimu menyenangkan :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")

                    elif payment_choise =="2":
                        internet =  f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        today = dt.date.today()
                        input_username =str(input("\nNama kamu : ")) 
                        input_taxt_id = str(input(f"\nMasukan id kamu ({id_pelanggan}) : "))
                      
                        if input_taxt_id == id_pelanggan:
                            print(f" Python Electric\n Username : {input_username}\n Id : {input_taxt_id}\n tax : ${internet}\n {today}")
                            answer = input("apakah kamu mau melakukan pembayaran? (yes / no)\n Pilihan kamu : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(internet)
                                result = f" \nPembayaran berhasil! saldo kamu = ${payment_status}"
                                thx = " Semoga harimu menyenagkan :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nTerimakasih telah berkunjung"   
                                thx = " Semoga harimu menyengangkan :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")
               
                    elif payment_choise =="3":
                        bill =  f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        today = dt.date.today()
                        input_username =str(input("\nNama kamu : ")) 
                        input_taxt_id = str(input(f"\nMasukan id kamu ({id_pelanggan}) : "))
                      
                        if input_taxt_id == id_pelanggan:
                            print(f"\n Python Net\n Username : {input_username}\n Id : {input_taxt_id}\n Bill : ${bill}\n {today}")
                            answer = input("apakah kamu mau melakukan pembayaran? (yes / no)\n Pilihan kamu : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(bill)
                                result = f" \nPembayaran berhasil! saldo kamu = ${payment_status}"
                                thx = " Semoga harimu menyengkan :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nTerimakasih telah berkunjung"   
                                thx = " Semoga harimu menyenangkan :D"
                                output = [text,thx]
                            
                            else : 
                              print("Invalid,please try again!")
               
                    elif payment_choise =="4":
                        bill =  f"{random.randint(10 , 200)}"
                        id_pelanggan = f"{random.randint(1000 , 9999)}"
                        today = dt.date.today()
                        input_username =str(input("\nNama kamu : ")) 
                        input_taxt_id = str(input(f"\nMasukan id kamu ({id_pelanggan}) : "))
                         
                        if input_taxt_id == id_pelanggan:
                            print(f"\n Python PAM\n Username : {input_username}\n Id : {input_taxt_id}\n Bill : ${bill}\n {today}")
                            answer = input("apakah kamu mau melakukan pembayaran? (yes / no)\n Pilihan kamu : ")
                            if answer=="yes" or answer =="Yes" or answer =="y" or answer =="Y":
                                payment_status =  balance - int(bill)
                                result = f" \nPembayaran berhasil! saldo kamu = ${payment_status}"
                                thx = " Semoga harimu menyengkan :D"
                                output = [result,thx]

                            elif answer=="no" or answer =="No" or answer =="n" or answer =="N":
                                text = "\nTerimakasih telah berkunjung"   
                                thx = " Semoga harimu menyenangkan :D"
                                output = [text,thx]
                            else : 
                              print("Invalid,please try again!")

              else:
                     print("Invalid,please try again!")

            else:
              print("\n Your Pin Invalid!")
              choices = input("\n Do you want to try again? yes or no\n Your Choose :")
              if choices =="yes" :
                  continue
              elif choices =="no":
                  break

              else:
                print("Invalid,Please Try Again!")            
        break  
    return output
            
def LK():
    while True:
      try:
       
          print("Bangun datar apa yang ingin kamu gunakan?\n 1) Persegi\n 2) Persegi panjang\n 3) Segitiga\n 4) Lingkaran")
          answer = input("Your Choose : ")
   
  
      except ValueError:
        print("\nError! Please Try Again!\n")
        continue
      else:
          if answer=="1":
              print("Kamu telah memilih Persegi")
              s = int(input("Masukan Sisi : "))
              k = s * 4
              l = s * s
          
          elif answer=="2":
              print("Kamu telah memilih Persegi Panjang")
              p = int(input("Masukan panjang : "))
              l = int(input("Masukan lebar   : "))
              
              k = 2 * ( p * l)
              l = p * l

          elif answer=="3":
              print("Kamu telah memilih Segitiga")
              a = int(input("Masukan alas     : "))
              t = int(input("Masukan tinggi   : "))
              s = int(input("Masukan sisi samping : "))              
              
              k = a + t + s 
              l = 1/2 * a * t
     

          elif answer=="4":
              print("Kamu telah memilih Persegi Panjang")
              r = float(input("Masukan jari-jari : "))
              phi = input("Masukan phi (22/7 , 3,14) : ")
              if phi =="22/7":
                  k = 2 * 22/7 * r
                  l = 1/2 * 22/7 * r * r   
              elif phi =="3,14":
                  k = 2 * 3.14 * r
                  l = 1/2 * 3.14 * r * r  

              else:

                  print("Hmmm")
       
          else:
              break    
                  
          output = [k,l]
   
       
          break
    return output
confirm = "y"
while confirm=="y":

    print('\n=================Kevien Tools=================\n')
    input_name = str(input("Please enter your name : "))
    y = input(f"\n Hi {input_name}! \n What do you want to do :\n Fun :\n 1.1 Love\n 1.2 Work\n Games :\n 2.1 Rock Sciccors and Pappe\n 2.2 Coming Soon!\n Calculating :\n 3.1 Temperature\n 3.2 Calculator\n 3.3 Bangun Datar\n Economy :\n 4.1 Python Bank\n Your Choose (Example : 1.1) : ")
    if y=="1.1":
      output_name = love()
      print("\nYour Name : {}".format(output_name[0]))
      print("Your Girlfriend : {}".format(output_name[1]))
      print("Love Status : {}".format(output_name[2]))

    elif y=="1.2":
      output_name = work()
      print("\nYour Name : {}".format(output_name[0]))
      print("Your Work : {}".format(output_name[1]))
      print("Your Salary : ${}".format(output_name[2]))
      print("Date Work : {}".format(output_name[3]))
    

    elif y=="2.1":
      output_name = suit()
      print("Your Result : {}".format(output_name[0]))
      
    elif y=="3.1":
      output_name = Temp()
      print("{}".format(output_name[0]))
   
    elif y=="3.2":
      output_name = Calc()
      print("\nYour Result : {}".format(output_name[0]))

    elif y=="3.3":
      output_name = LK()
      print("\nKeliling : {}".format(output_name[0]))
      print("\nLuas     : {}".format(output_name[1]))

    elif y=="4.1":
      output_name = Atm()
      print("{}".format(output_name[0]))
      print("{}".format(output_name[1]))

    else:
        print("\nError! Please Try Again!\n")
      
    coba = input("Would you like to try again? Yes or No! : ")
    if coba =="N" or coba=="n" or coba=="No" or coba=="NO":
      break

    elif coba =="Y" or coba=="y" or coba=="Yes" or coba =="YES":
      continue

    else:
      print("PUSING GW SAMA LU!,please Try again!")      
      break
else:
      print("Try Again!")    

print("Akhir Dari Pemograman! Terimakasih :D")      