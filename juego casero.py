import time 

while True:
  try:
   print("===juego de python===\n")
   print("1.Facil")
   print("2.Dificil")
   elegir = int(input("elige una opción: "))
   time.sleep(1)
   
   if elegir==2:
     print("El modo dificil no esta disponible por el momento")
     break 

   if elegir>2:
    print("[*]advertencia......")
    time.sleep(1)
    print("solo existen 2 opciones ")
    time.sleep(1)
    
   if elegir==1:
    print("[*]cargando juego......\n")
    time.sleep(3)
  
   print("====Elige tu ataque====\n")
   print("1.Fuego")
   print("2.Agua")
   print("3.Bolas de hielo")
   print("4.Bolas de fuego")
   print("5.Escudo y armadura potente")
   elegir_primer_ataque = int(input("Elige el ataque de tu oponente: "))
   elegir_segundo_ataque = int(input("Elige tu propio ataque: "))
   time.sleep(1)
      
   if elegir_primer_ataque and elegir_segundo_ataque>5:
    print("[*]advertencia......\n")
    time.sleep(1)
    print("solo existen 5 opciones de menú")
    time.sleep(1)

   if elegir_primer_ataque==1 and  elegir_segundo_ataque==1:
    print("[*]Empate!\n")
    time.sleep(1)
    print("Tu oponente eligio el mismo ataque!")
    time.sleep(1)
  
   elif elegir_primer_ataque==2 and elegir_segundo_ataque==2:
     print("[*]espere un momento......\n")
     time.sleep(1)
     print("Empate!\n")
     time.sleep(1)
   
   elif elegir_primer_ataque==3 and elegir_segundo_ataque==3:
     print("[*]espere un momento......\n")
     time.sleep(2)
     print("Empate!\n")
     time.sleep(1)

   elif elegir_primer_ataque==4 and elegir_segundo_ataque==4:
      print("[*]espere un momento......\n")
      time.sleep(2)
      print("Empate!\n")
      time.sleep(1)
   
   elif elegir_primer_ataque==5 and elegir_segundo_ataque==5:
      print("[*]espere un momento......\n")
      time.sleep(2)
      print("Empate!\n")
      time.sleep(1)

   elif elegir_primer_ataque==1 and   elegir_segundo_ataque==2:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("Ganaste, el fuego pierde contra el agua!\n")
    time.sleep(1)
  
   elif elegir_primer_ataque==1 and elegir_segundo_ataque==3:
    print("[*]espere un momento......")
    time.sleep(1)
    print("Ganaste, las bolas de hielo desaparece el fuego!\n")
    time.sleep(1)

   elif elegir_primer_ataque==1 and elegir_segundo_ataque==4:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("perdiste, las bolas de fuego vencen al fuego!\n")    
    time.sleep(1)
  
   elif elegir_primer_ataque==1 and   elegir_segundo_ataque==5:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("Ganaste, el escudo y armadura soportan el fuego\n")    
    time.sleep(1) 
  
   elif elegir_primer_ataque==2 and elegir_segundo_ataque==3:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("perdiste, el agua derrite al hielo!\n")
    time.sleep(1)
  
   elif elegir_primer_ataque==2 and elegir_segundo_ataque==4:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("perdiste, el agua apaga las bolas de fuego\n")
    time.sleep(1)
  
   elif elegir_primer_ataque==2 and elegir_segundo_ataque==5:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("Evaluando los ataques......")
    time.sleep(1)
    print("El agua no puede contra un escudo y armadura!")
  
   elif elegir_primer_ataque==3 and elegir_segundo_ataque==4:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("Evaluando los ataques\n")
    time.sleep(1)
    print("Ganaste, bolas de hielo vence las bolas de fuego\n")
    time.sleep(1)
  
   elif elegir_primer_ataque==3 and elegir_segundo_ataque==5:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("Evaluando los ataques\n")
    time.sleep(1)
    print("Ganaste, el escudo y armadura vence a las bolas de hielo\n")
    time.sleep(1)

   elif elegir_primer_ataque==4 and elegir_segundo_ataque==5:
    print("[*]espere un momento......\n")
    time.sleep(1)
    print("Evaluando los ataques\n")
    time.sleep(1)
    print("Ganaste, el escudo y armadura vence a las bolas de fuego\n")
    time.sleep(1)  
   
   elif elegir_primer_ataque==5 and elegir_segundo_ataque==4:
     print("[*]espere un momento......")
     time.sleep(1)
     print("Evaluando los ataques......\n")
     time.sleep(2)
     print("perdiste, escudo y armadura vencen a las bolas de fuego\n")
     time.sleep(1)

   elif elegir_primer_ataque==5 and elegir_segundo_ataque==3:
     print("[*]espere un momento......\n")
     time.sleep(1)
     print("Evaluando los ataques......\n")
     time.sleep(2)
     print("perdiste, escudo y armadura vencen a las bolas de hielo\n")
     time.sleep(1)

   elif elegir_primer_ataque==5 and elegir_segundo_ataque==2:
     print("[*]espere un momento......\n")
     time.sleep(2)
     print("Evaluando los ataques......\n")
     time.sleep(2)
     print("perdiste, escudo y armadura vencen al agua") 
   
   elif elegir_primer_ataque==5 and elegir_segundo_ataque==1:
     print("[*]espere un momento......\n")
     time.sleep(2)
     print("Evaluando los ataques......\n")
     time.sleep(2)
     print("perdiste, escudo y armadura vencen al fuego\n")
     time.sleep(1)
    
    elif elegir_primer_ataque==4 and elegir_segundo_ataque==3:
        print("[*]espere un momento......\n")
     time.sleep(2)
     print("Evaluando los ataques......\n")
     time.sleep(2)
     print("perdiste, escudo y armadura vencen al fuego\n")
     time.sleep(1)
        
    
  except ValueError:
    print("usted escribio algo mal, eliga las opciones con numeros postivos\n")

  except Exception as error:
    print("algo salio mal intentelo otra vez",error)  
