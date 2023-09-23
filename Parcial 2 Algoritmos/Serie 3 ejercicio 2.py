def calcular_suma(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma
def calcular_promedio(valores):
    suma = calcular_suma(valores)
    promedio = suma / len(valores)
    return promedio
def main():
    valores_str = input("Ingrese valores separados por comas: ")
    valores = [float(valor) for valor in valores_str.split(',')]
    suma = calcular_suma(valores)
    promedio = calcular_promedio(valores)
    print(f"Suma: {suma}")
    print(f"Promedio: {promedio}")

if __name__ == "__main__":
    main()
