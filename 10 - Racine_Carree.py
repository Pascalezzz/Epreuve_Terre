import sys
import math

#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur, entrez qq chose svp.")
   sys.exit()
   
#Si le nombre d'argument > 2, print "erreur"
if len(sys.argv) > 2:
    print("erreur, trop de chiffres")
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

#Pas d'entiers négatifs
if int(sys.argv[1]) < 0:
    print("erreur, pas d'entiers négatifs.")
    sys.exit()

#Racine carrée
print(math.sqrt(int(sys.argv[1])))