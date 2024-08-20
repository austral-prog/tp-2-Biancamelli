def change():
    gasto = 23.75
    Dinero_recibido: 100
    Pesos: 76
    Centavos:25
    gasto= float("23.75\n")
    dinero_recibido= float("100\n")
    vuelto= dinero_recibido-gasto
    pesos= int(vuelto)
    Centavos=int(round((vuelto-pesos)*100))
    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{Centavos}")
