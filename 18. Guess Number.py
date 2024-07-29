max_intentos = 5

intentos = 0

adivinanza = 0

while adivinanza != 6 and intentos < max_intentos:
    adivinanza = int(input("Guess the number: "))
    intentos += 1

if adivinanza == 6:
    print("You got it!")
else:
    print("Sorry, you've used all your attempts.")