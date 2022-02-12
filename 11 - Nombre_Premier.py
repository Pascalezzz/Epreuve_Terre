import sys

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

a = sys.argv[1]
k = int(sys.argv[1])

# 1 not being a prime number, is ignored
if k > 1:
    for i in range(2, int(k/2)+1):
         if (k % i) == 0:
            print("Non, " + a + " n'est pas un nombre premier")
            break
    else:
        print("Oui, " + a + " est un nombre premier")

else:
    print("Non, " + a + " n'est pas un nombre premier")