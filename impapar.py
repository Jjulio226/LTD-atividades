print("Verificador de numeros, par ou impa.")
n1= int(input("Insira um número: "))
print("_____________________________")
n2= int(input("Insira outro numero: "))
print("-----------------------------")
soma = n1 + n2
if soma %2 == 0:
    print(f"O numero {soma} é par.")
else:
    print(f"{soma} é impar.")
print("---------------------------")

