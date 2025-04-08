idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura :"))
peso = float(input("Digite seu peso: "))

imc = peso % (altura * altura)

print(f"seu resultado é: {imc}")

if imc<18.5:
    print(f"{imc} pode ser considerado magreza.")
elif imc >= 18.5 and 24.9:
    print(f"{imc} seu peso está normal")
elif imc >= 25 and 29.9:
    print(f"{imc} está com sobrepeso")
elif imc >= 30 and 34.9:
    print(f"{imc} é considerado obesidade grau I")
elif imc >= 35 and 39.9:
    print(f"{imc} é considerado obesidade grau II")
elif imc >= 40:
    print(f"{imc} obesidade grau III")
