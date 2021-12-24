import random
import datetime as dt


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

       
        
        break
    return output
        
