puntos = {'Gryffindor': 0, 'Ravenclaw': 0, 'Hufflepuff': 0, 'Slytherin': 0}

respuesta1 = int(input("Q1) Do you like Dawn or Dusk?\n1) Dawn\n2) Dusk\nIngrese su respuesta (1 o 2): "))
if respuesta1 == 1:
    puntos['Gryffindor'] += 1
    puntos['Ravenclaw'] += 1
elif respuesta1 == 2:
    puntos['Hufflepuff'] += 1
    puntos['Slytherin'] += 1
else:
    print("Entrada incorrecta")

respuesta2 = int(input("Q2) When I’m dead, I want people to remember me as:\n1) The Good\n2) The Great\n3) The Wise\n4) The Bold\nIngrese su respuesta (1-4): "))
if respuesta2 == 1:
    puntos['Hufflepuff'] += 2
elif respuesta2 == 2:
    puntos['Slytherin'] += 2
elif respuesta2 == 3:
    puntos['Ravenclaw'] += 2
elif respuesta2 == 4:
    puntos['Gryffindor'] += 2
else:
    print("Entrada incorrecta")

respuesta3 = int(input("Q3) Which kind of instrument most pleases your ear?\n1) The violin\n2) The trumpet\n3) The piano\n4) The drum\nIngrese su respuesta (1-4): "))
if respuesta3 == 1:
    puntos['Slytherin'] += 4
elif respuesta3 == 2:
    puntos['Hufflepuff'] += 4
elif respuesta3 == 3:
    puntos['Ravenclaw'] += 4
elif respuesta3 == 4:
    puntos['Gryffindor'] += 4
else:
    print("Entrada incorrecta")

casa = max(puntos, key=puntos.get)

print(f"\nLa casa con más puntos es: {casa}")