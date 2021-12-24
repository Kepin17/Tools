
import random
import datetime as dt

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
            