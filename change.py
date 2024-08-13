def cambio():
    gasto= 23.75
    dinero= 100

    Vuelto= dinero-gasto

    Pesos=int(Vuelto)
    Centavos=int((Vuelto-Pesos)*100)

    print("\nVuelto\n")
    print(f"Pesos:\n{Pesos}")
    print(f"Centavos:\n{Centavos}")
