soma=0
print ("Digite os Dez numeros que deseja saber a soma dos quadrados.")
for i in range (1,11):
   
    numero=int(input(f" Numero {i} :"))
    
    soma = soma + (numero**2)
print (f" A soma dos quadrados é : {soma}")