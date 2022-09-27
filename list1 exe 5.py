import math
tamanhodaarea=int(input(" \nTamanho da Aréa em metros quadrados que deseja ser pintada : "))
litroslata=18
litrosgalao=3.6
needlitros=float(tamanhodaarea/6)*1.10


somentelata=math.ceil(needlitros/litroslata)
precosomentelata =somentelata*80
litrossomentelata=somentelata*litroslata

somentegalao=math.ceil(needlitros/litrosgalao)
precosomentegalao=somentegalao*25
litrossomentegalao=somentegalao*litrosgalao


qtdlataE=int((needlitros)/litroslata)
faltalitros=needlitros- (qtdlataE*18)
ecogalao=math.ceil(faltalitros/litrosgalao)

precoeconomico=(qtdlataE*80)+(ecogalao*25)
litroseconomico=(qtdlataE*litroslata)+(ecogalao*litrosgalao)
repetirpergunta=1

while repetirpergunta>0 :
    print(" Digite 1 para comprar somente Latas de 18 Litros.")
    print(" Digite 2 para comprar somente Galões de 3,6 Litros.")
    print(" Digite 3 para comprar entre Latas e Galões Modo mais econômico.")
    n=int(input(" Aguardadndo número da Opção : "))

    if n==1:
        print(f"\n Total de {litrossomentelata}Litros")
        print(f"  Valor de R$ {precosomentelata} ")
        repetirpergunta=0
    elif n==2:
        print(f"\n Total de {litrossomentegalao:.2f}Litros")
        print(f"  Valor de R$ {precosomentegalao} ")
        repetirpergunta=0
    elif n==3 :
        print(f"\n Total de {litroseconomico:.2f}Litros")
        print(f"  Valor de R$ {precoeconomico} ")
        repetirpergunta=0
    else : 
        print("\n Número inserido incorrespondente.")
        repetirpergunta=1   
