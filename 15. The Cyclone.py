altura_minima = 137 
creditos_requeridos = 10

altura = float(input("¿Cuál es tu altura en cm? "))
creditos = int(input("¿Cuántos créditos tienes? "))

if altura >= altura_minima and creditos >= creditos_requeridos:
    print("¡Disfruta el viaje!")
elif altura < altura_minima and creditos >= creditos_requeridos:
    print("No eres lo suficientemente alto para viajar")
elif altura >= altura_minima and creditos < creditos_requeridos:
    print("No tienes suficientes créditos")
else:
    print("No cumples con ninguno de los requisitos")
