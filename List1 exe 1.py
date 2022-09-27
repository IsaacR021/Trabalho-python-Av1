
sexo =int(input("\nQual seu sexo? Digite (1) Masculino  ou  (2) Feminino ? "))

altura= float(input("\nDigite sua altura: "))


pesomasculino = float((72.7 * altura)-58)
pesofeminino = float((62.1 * altura)-44.7)

if sexo ==1:
    print(f"\nSeu peso ideal é : {pesomasculino:.2f}")
elif sexo ==2:
    print(f"\nSeu peso ideal é : {pesofeminino:.2f}")
else:
    print("\nSexo incorrespondente")
