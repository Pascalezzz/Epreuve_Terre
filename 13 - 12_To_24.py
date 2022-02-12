#Comment régler le probleme de si l'utilisateur rentre n'importe quoi ?

import sys

#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur, entrez qq chose svp.")
   sys.exit()

if len(sys.argv[1]) < 3:
    print("entrer une heure au format 12h svp")
    sys.exit()

#Empecher l'user d'entrer n'importe quoi   
if sys.argv[1][2] != ":":
    print("entrer une heure au format 12h svp")
    sys.exit()
    
#Heures réelles seulement
if int(sys.argv[1][:2]) > 12:
    print("entrer une heure au format 12h svp")
    sys.exit()

if int(sys.argv[1][3:5]) > 60:
    print("entrer une heure au format 12h svp")
    sys.exit()

#Midi et minuit
heure = str(sys.argv[1])
    
def convert(heure):

      if heure[-2:] == "AM" and heure[:2] == "12":
         return "00" + heure[2:-2]

      elif heure[-2:] == "AM":
         return heure[:-2]

      elif heure[-2:] == "PM" and heure[:2] == "12":
         return heure[:-2]
        
      else:
          return str(int(heure[:2]) + 12) + heure[2:8]

#convertir heure

print(convert(sys.argv[1]))



    
