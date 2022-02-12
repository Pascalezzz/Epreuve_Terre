import sys



#Si l'argument est vide, "erreur"
if len(sys.argv) == 1:
   print("erreur, entrez qq chose svp.")
   sys.exit()

if len(sys.argv) <= 3:
    print("entrez une liste de 3 entiers svp.")
    sys.exit()

#Si l'argument est une string, print "erreur"
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()
        
if (is_integer(sys.argv)) == False:
    print("erreur, faut mettre des chiffres.")
    sys.exit()
    
list = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])]

def findMiddle(list):
    middle = float(len(list))/2
    if middle % 2 != 0:
        return list[int(middle - .5)]
    else:
        return (list[int(middle)], list[int(middle-1)])
        
print(findMiddle(sorted(list)))