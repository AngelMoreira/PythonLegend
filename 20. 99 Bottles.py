for i in range(99, 0, -1):
    if i > 1:
        print(f"{i} botellas de cerveza en la pared, {i} botellas de cerveza.")
        print("Toma una y pásala alrededor,")
        print(f"{i - 1} botellas de cerveza en la pared.\n")
    else:
        print(f"1 botella de cerveza en la pared, 1 botella de cerveza.")
        print("Tómala y pásala alrededor,")
        print("No quedan botellas de cerveza en la pared.\n")

