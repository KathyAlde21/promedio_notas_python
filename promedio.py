def pedir_nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero} (de 1 a 7): "))
            if 1 <= nota <= 7:
                return nota
            else:
                print("⚠️ La nota debe estar entre 1 y 7. Inténtalo de nuevo.")
        except ValueError:
            print("❌ Debes ingresar un número. Inténtalo de nuevo.")

while True:
    # Pedimos las notas con validación
    nota1 = pedir_nota(1)
    nota2 = pedir_nota(2)
    nota3 = pedir_nota(3)
    nota4 = pedir_nota(4)

    # Calculamos el promedio
    promedio = (nota1 + nota2 + nota3 + nota4) / 4

    # Mostramos si aprobó o reprobó
    if promedio > 4.0:
        print(f"✅ Aprobado con promedio de {promedio:.2f}")
    else:
        print(f"❌ Reprobó con promedio de {promedio:.2f}")

    # Preguntamos si se desea continuar
    continuar = input("¿Desea ingresar otro estudiante? (S/N): ").strip().upper()
    if continuar == "N":
        break
