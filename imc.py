idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura :"))
peso = float(input("Digite seu peso em kg: "))

imc = peso % (altura * altura)

print(f"seu resultado é: {imc}")

if imc < 18.5:
   print(f"Classificação: Magreza.")
elif 18.5 <= imc <= 24.9:
    print(f"Classificação: Peso normal.")
elif 25 <= imc <= 29.9:
    print(f"Classificação: Sobrepeso.")
elif 30 <= imc <= 34.9:
     print(f"Classificação: Obesidade grau I.")
elif 35 <= imc <= 39.9:
     print(f"Classificação: Obesidade grau II.")
else: # Para IMC >= 40
     print(f"Classificação: Obesidade grau III.")
