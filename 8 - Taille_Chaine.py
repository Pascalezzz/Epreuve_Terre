import sys
        
#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur.")
   sys.exit()
    
#Si le nombre d'argument > 2, print "erreur"
if len(sys.argv) > 2:
    print("erreur.")
    sys.exit()
    
#Si l'argument est une int, print "erreur"
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
if (is_integer(sys.argv[1])) == True:
    print("erreur")
    sys.exit()

#Finalement, donné la longueur de la string
print(len(sys.argv[1]))