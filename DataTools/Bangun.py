           
def Bangun():
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