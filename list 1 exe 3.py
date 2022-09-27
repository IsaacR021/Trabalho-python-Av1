ganhoporhora=float(input("\n Quanto Você ganha por hora ? R$ "))
totaldehoras=float(input("\n Total de horas trabalhadas no mês ? R$ "))
salariobruto=ganhoporhora*totaldehoras
descontodeir=(salariobruto*11)/100
descontoinss=(salariobruto*8)/100
descontosindicato=(salariobruto*5)/100
salarioliquido=salariobruto-descontodeir-descontoinss-descontosindicato


print (f" \n Seu salário bruto é R$: {salariobruto}")
print (f" \n Desconto do IR R$: {descontodeir}")
print (f" \n Desconto do Inss R$: {descontoinss}")
print (f" \n Desconto do Sindicato R$: {descontosindicato}")
print (f" \n Seu salário líquido é R$: {salarioliquido}")
