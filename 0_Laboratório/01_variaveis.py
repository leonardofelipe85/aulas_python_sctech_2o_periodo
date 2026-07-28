#idade = 20 

#outra_idade = idade

#idade = 30

#print(idade)
#print(outra_idade)

#tem_carteira = False

#if idade >= 18 and tem_carteira:
 #   print("Pode dirigir")
#else:
#    print("Não pode dirigir")

#funcionarios = ["Ana", "Bruno", "Carla", "Diego"]

#for funcionario in funcionarios: 
#    print("Funcionario: ", funcionario)


#nomes = ["nome1", "nome2", "nome3", "nome4", "nome5"]

#for indice in range(len(nomes)):
    # aqui dentro, "indice" vai valer 0, 1, 2, 3, 4 — um por vez
    # e nomes[indice] te dá o nome que está naquela posição
 #   print("Posição", indice, ":", nomes[indice])

#saldo = 100

#while saldo > 0: 
 #   print("Saldo", saldo)
  #  saldo = saldo -30


campanhas = ["Rede de Pesquisa", "Google Shopping", "Rede de Display", "YouTube"]
cliques = [450, 368, 478, 388]
ctr = [1.2, 2.2, 3.8, 3.7]
campanha_ativa = True

campanhas.insert(0, "Campanha Nova")
ctr.insert(0, 3.7)
cliques.insert(0, 458)

campanhas.append("Campanha Instagram")
ctr.append(2.5)
cliques.append(320)

campanhas.remove("Rede de Display")
del ctr[3]
del cliques [3]

for i in range(len(campanhas)): 

    if ctr[i] >=3: 
        classificacao = "Excelente"
    elif ctr[i] >=1.5: 
        classificacao = "Boa"
    else: 
        classificacao = "Precisa de Otimização"

    print(campanhas[i], "-CTR: ", ctr[i], "-", classificacao)

