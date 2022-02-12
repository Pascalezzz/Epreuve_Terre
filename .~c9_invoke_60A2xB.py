import sys

if int(sys.argv[2]) == 0:
    print("erreur.")
    sys.exit()
    
a = (int(sys.argv[1]) / int(sys.argv[2]))
b = (int(sys.argv[1]) % int(sys.argv[2]))
    
check_int = isinstance(a, int)
if check_int == False:
    print("erreur.")
    sys.exit()
    
print("{}{}".format("résultat: ", int(a)))
print("{}{}".format("reste: ", int(b)))