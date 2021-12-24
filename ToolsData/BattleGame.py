import random

def Battle():
    while True:
        try:
 
          print("\nSilahkan pilih hero kamu :\nA) Wiro Sableng\nB) Ninja\nC) Karina\nD) Ganyu ")
          Hero = input("Your Choose A/B/C/D: ")
        except ValueError:
            print("Error,please try again!")
            continue
        else:
            healtbar1 = random.randint(10,100)
            attack1 = random.randint(10,100)
            healtbar2 = random.randint(10,100)
            attack2 = random.randint(10,100)
            Attack1 = healtbar1 - attack2
            Attack2 = healtbar2 - attack1
            if Hero =="A":
                heroName = "Wiro Sableng"
                hero2 = ["Octo","Reamur","Yuki"]
                player2 = random.choice(hero2)
                if Attack1 < 0 and Attack2 < 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage \nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        draw = F"\nDraw!!"
                        output = [Battle,status , draw]
        
        
                
                elif Attack1 < 0 and Attack2 > 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        lose = F"\nKalah!!"
                        output = [Battle,status , lose]
        
                elif Attack1 > 0 and Attack2 < 0:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
              
                elif Attack1 > Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
       
                elif Attack1 < Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        win = f"\nKalah!!"
                        output = [Battle,status , win]
           
            elif Hero =="B":
                heroName = "Ninja"
                hero2 = ["Octo","Reamur","Yuki"]
                player2 = random.choice(hero2)
                if Attack1 < 0 and Attack2 < 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage \nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        draw = F"\nDraw!!"
                        output = [Battle,status , draw]
        
                
                elif Attack1 < 0 and Attack2 > 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        lose = F"\nKalah!!"
                        output = [Battle,status , lose]
        
                elif Attack1 > 0 and Attack2 < 0:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
              
                elif Attack1 > Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
       
                elif Attack1 < Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        win = f"\nKalah!!"
                        output = [Battle,status , win]
       
            elif Hero =="C":
                heroName = "Karina"
                hero2 = ["Octo","Reamur","Yuki"]
                player2 = random.choice(hero2)

                if Attack1 < 0 and Attack2 < 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage \nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        draw = F"\nDraw!!"
                        output = [Battle,status , draw]
  
                
                elif Attack1 < 0 and Attack2 > 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        lose = F"\nKalah!!"
                        output = [Battle,status , lose]
        
                elif Attack1 > 0 and Attack2 < 0:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
        
                elif Attack1 > Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
       
                elif Attack1 < Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        win = f"\nKalah!!"
                        output = [Battle,status , win]
         
            elif Hero =="D":
                heroName = "Ganyu"
                hero2 = ["Octo","Reamur","Yuki"]
                player2 = random.choice(hero2)
                if Attack1 < 0 and Attack2 < 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage \nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        draw = F"\nDraw!!"
                        output = [Battle,status , draw]
        
                elif Attack1 > Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
            
                
                elif Attack1 < 0 and Attack2 > 0:

                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        lose = F"\nKalah!!"
                        output = [Battle,status , lose]
        
                elif Attack1 > 0 and Attack2 < 0:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : {Attack1}\n\nYou Attack and give {attack1} damage\nEnemy Health : 0"
                        win = f"\nMENANG!!"
                        output = [Battle,status , win]
       
                elif Attack1 < Attack2:
                        Battle = f"\nBattle start\n Hero 1 : {heroName}\n Hero 1 Health : {healtbar1}\n Hero 1 Attack : {attack1}\n\n Hero 2 : {player2}\n Hero 2 Health : {healtbar2}\n Hero 2 Attack : {attack2} "
                        Attack1 = healtbar1 - attack2
                        Attack2 = healtbar2 - attack1
                        status = f"\n{50*'='}\nEnemy attack and give {attack2} damage\nYour Health : 0\n\nYou Attack and give {attack1} damage\nEnemy Health : {Attack2}"
                        win = f"\nKalah!!"
                        output = [Battle,status , win]
        
                  
            else:
                    print("Option invalid!")


        break        
    return output  