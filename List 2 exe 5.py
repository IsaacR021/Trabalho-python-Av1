ganhoporhora=float(input("\n Quanto Você ganha por hora ? R$ "))
totaldehoras=float(input("\n Total de horas trabalhadas no mês ? R$ "))
salariobruto=ganhoporhora*totaldehoras
descontodeir=(salariobruto*11)/100
descontoinss=(salariobruto*8)/100
descontosindicato=(salariobruto*5)/100
salarioliquido=salariobruto-descontodeir-descontoinss-descontosindicato


print (f" \nSeu salário bruto é R$: {salariobruto}")
print (f" \nDesconto do IR R$: {descontodeir}")
print (f" \nDesconto do Inss R$: {descontoinss}")
print (f" \nDesconto do Sindicato R$: {descontosindicato}")
print (f" \nSeu salário líquido é R$: {salarioliquido}")
