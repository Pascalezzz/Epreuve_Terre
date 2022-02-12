import sys

if int(sys.argv[2]) == 0:
    print("erreur.")
    sys.exit()
    
a = (int(sys.argv[1]) / int(sys.argv[2]))
b = (int(sys.argv[1]) % int(sys.argv[2]))

if int(a) == 0:
    print("erreur.")
    sys.exit()
    
print("résultat: ", int(a))
print("reste: ", int(b))