import sys 

if len(sys.argv) < 2:
    print ("Tu ne me la mettras pas à l'envers.")
    sys.exit()

a = sys.argv[1]    
    
if len(sys.argv) > 1:
    try:
        val = int(a)
    except ValueError:
        print("Tu ne me la mettras pas à l'envers.")
        sys.exit()
    else:
        if (int(a) % 2 == 0):
            print("pair")
        elif (int(a) % 2 != 0):
            print("impair")