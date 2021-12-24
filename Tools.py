from ToolsData import Atm , work , love , Calc , suit , Temp , Bangun , Battle


 
confirm = "y"
while confirm=="y":

    print('\n=================Kevien Tools=================\n')
    input_name = str(input("Please enter your name : "))
    y = input(f"\n Hi {input_name}! \n What do you want to do :\n Fun :\n 1.1 Love\n 1.2 Work\n Games :\n 2.1 Rock Sciccors and Pappe\n 2.2 Battle game\n 2.3 Coming Soon!\n Calculating :\n 3.1 Temperature\n 3.2 Calculator\n 3.3 Bangun Datar\n Economy :\n 4.1 Python Bank\n Your Choose (Example : 1.1) : ")
    if y=="1.1":
      output_name = love()
      print(50*"=","\nYour Name : {}".format(output_name[0]))
      print("Your Girlfriend : {}".format(output_name[1]))
      print("Love Status : {}".format(output_name[2]))

    elif y=="1.2":
      output_name = work()
      print(50*"=","\nYour Name : {}".format(output_name[0]))
      print("Your Work : {}".format(output_name[1]))
      print("Your Salary : ${}".format(output_name[2]))
      print("Date Work : {}".format(output_name[3]))
    

    elif y=="2.1":
      output_name = suit()
      print(50*"=","\nYour Result : {}".format(output_name[0]))
      
    elif y=="3.1":
      output_name = Temp()
      print(50*"=","\n{}".format(output_name[0]))
   
    elif y=="3.2":
      output_name = Calc()
      print(50*"=","\nYour Result : {}".format(output_name[0]))

    elif y=="3.3":
      output_name = Bangun()
      print(50*"=","\nKeliling : {}".format(output_name[0]))
      print("\nLuas     : {}".format(output_name[1]))

    elif y=="4.1":
      output_name = Atm()
      print("{}".format(output_name[0]))
      print("{}".format(output_name[1]))
  
    elif y=="2.2":
      output_name = Battle()
      print("{}".format(output_name[0]))
      print("{}".format(output_name[1]))
      print("{}".format(output_name[2]))

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