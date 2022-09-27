
saque = int(input("\n Valores para retirada  \n Valor Mínimo : R$ 10,00 \n Valor Máximo : R$ 600,00 \n Quanto deseja Sacar ? R$"))

if saque < 10 :
    print ("Quantia de saque desajada não atingiu o valor mínimo de saque")

elif  saque > 600:
    print ("Quantia de saque desejada ultrapassa o valor máximo de saque")

else  :

    notasde100 = int(saque / 100)
    saque = saque - (notasde100*100)
        
    notasde50 = int(saque/50)
    saque = saque - (notasde50*50)
    
    notasde10 = int(saque/10)
    saque = saque - (notasde10*10)
    
    notasde5 = int(saque/5)
    saque = saque - (notasde5*5)
    
    notasde1 = int(saque/1)
    saque = saque - (notasde1*1)
    
    
        
    if notasde100 >=1 :
        print(F" {notasde100} Notas de R$100,00")
    if notasde50 >=1 :
        print(F" {notasde50} Notas de R$50,00")
    if notasde10 >=1 :
        print(F" {notasde10} Notas de R$10,00")
    if notasde5 >= 1 :
        print(F" {notasde5} Notas de R$5,00")
    if notasde1 >=1 :
        print(F" {notasde1} Notas de R$1,00")

