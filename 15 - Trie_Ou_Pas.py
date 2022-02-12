import sys


#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur, entrez qq chose svp.")
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



a = len(sys.argv)
list_number = sys.argv[1:a]



flag = 0
list_number1 = list_number[:]
list_number.sort()
if (list_number1 == list_number):
    flag = 1

if (flag) :
    print ("Triée !")
else :
    print ("Pas triée")

