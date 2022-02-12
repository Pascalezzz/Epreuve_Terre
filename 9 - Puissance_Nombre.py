import sys
import math

#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur, entrez qq chose svp.")
   sys.exit()
   
#Si le nombre d'argument > 3, print "erreur"
if len(sys.argv) > 3:
    print("Un chiffre de trop pour ta puissance.")
    sys.exit()
    
#Si l'argument est une string, print "erreur"
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
if (is_integer(sys.argv[1])) == False:
    print("erreur, faut mettre des chiffres.")
    sys.exit()
    
if (is_integer(sys.argv[2])) == False:
    print("erreur, faut mettre des chiffres.")
    sys.exit()

#Pas d'exposant négatif
if int(sys.argv[2]) < 0:
    print("erreur, pas d'éxposant négatif.")
    sys.exit()

#Puissance de arg1 par arg2
print(math.pow(int(sys.argv[1]), int(sys.argv[2])))