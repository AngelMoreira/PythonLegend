# Write code below 💖

pesos_a_usd = 0.00021
soles_a_usd = 0.27
reales_a_usd = 0.20

cantidad_pesos = float(input("What do you have left in pesos?: "))
cantidad_soles = float(input("What do you have left in soles?: "))
cantidad_reales = float(input("What do you have left in reais?: "))

usd_de_pesos = cantidad_pesos * pesos_a_usd
usd_de_soles = cantidad_soles * soles_a_usd
usd_de_reales = cantidad_reales * reales_a_usd

total_usd = usd_de_pesos + usd_de_soles + usd_de_reales

print(f"{total_usd:.2f}")
