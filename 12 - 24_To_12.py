#Comment régler le probleme de si l'utilisateur rentre n'importe quoi ?

import sys

#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur, entrez qq chose svp.")
   sys.exit()

if len(sys.argv[1]) < 3:
    print("entrer une heure au format 24h svp")
    sys.exit()

#Empecher l'user d'entrer n'importe quoi   
if sys.argv[1][2] != ":":
    print("entrer une heure au format 24h svp")
    sys.exit()
    
#Heures réelles seulement
if int(sys.argv[1][:2]) > 23:
    print("entrer une heure au format 12h svp")
    sys.exit()

if int(sys.argv[1][3:5]) > 60:
    print("entrer une heure au format 12h svp")
    sys.exit()
    
    
    
#Si c'est midi ou minuit
if sys.argv[1][:2] == "00":
    print("12" + str(sys.argv[1][2:]) + "AM")
    sys.exit()
if sys.argv[1][:2] == "12":
    print("12" + str(sys.argv[1][2:]) + "PM")
    sys.exit()
    
#Retirer 12 de l'heure donnée si arg > 12
#Ajouter le AM ou le PM
#Donner l'heure
a=int(sys.argv[1][:2]) - 12
b=int(sys.argv[1][:2])

if int(sys.argv[1][:2]) >= 12:
    print(str(a) + str(sys.argv[1][2:]) + "PM")
    sys.exit()
    
if int(sys.argv[1][:2]) <= 12:
    print(str(b) + str(sys.argv[1][2:]) + "AM")
    sys.exit()