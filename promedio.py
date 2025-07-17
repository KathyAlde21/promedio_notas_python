def pedir_nota(numero):
    while True:
        try:
            nota = float(input(f"Ingrese la nota {numero} (entre 1 y 7): "))
            if 1 <= nota <= 7:
                return nota
            else:
                print("⚠️ Error: La nota debe estar entre 1 y 7.")
        except ValueError:
            print("⚠️ Error: Debes ingresar un número válido.")

def calcular_promedio():
    while True:
        print("\n--- Ingreso de notas del estudiante ---")
        
        nota1 = pedir_nota(1)
        nota2 = pedir_nota(2)
        nota3 = pedir_nota(3)
        nota4 = pedir_nota(4)

        promedio = (nota1 + nota2 + nota3 + nota4) / 4

        if promedio >= 4.0:
            print(f"✅ Aprobado con promedio de {promedio:.2f}")
        else:
            print(f"❌ Reprobó con promedio de {promedio:.2f}")

        continuar = input("¿Desea ingresar otro estudiante? (S/N): ").strip().upper()
        if continuar == "N":
            break

calcular_promedio()
