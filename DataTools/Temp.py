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
