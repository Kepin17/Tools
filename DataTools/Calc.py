
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
