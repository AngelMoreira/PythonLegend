ph = float(input("Ingrese un valor de pH entre 0 y 14: "))
if ph > 7:
    print("Básico")
elif ph < 7:
    print("Ácido")
else:
    print("Neutral")