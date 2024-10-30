

#royal_flushFEITO
#straight_flush FEITO
#four_of FEITO
#fullhouse FEITO
#flush FEITO
#straight FEITO
#three_of FEITO
#two_pair FEITO
#pair FEITO
#high_card

maos_teste = [
    ["AC", "05C", "10C", "07C", "03S"],
    ["02C", "03D", "04S", "05H", "02D"],
    ["02C", "03D", "04S", "03H", "02D"],
    ["05S", "04C", "05D", "04S", "04H"],
    ["03H", "07H", "06S", "04D", "05S"],
    ["AC", "05C", "10C", "07C", "03C"],
    ["08D", "05C", "05H", "08S", "08H"],
    ["03D", "07H", "07S", "07C", "07D"],
    ["AS", "10S", "QS", "KS", "JS"],
]
#funcao para o naipe da carta
def naipe(carta):
  return carta[-1]
#funcao para o valor da carta, letras viram numeros
def valor(carta):
  if carta[0] == "A":
    return 14
  if carta[0] == "K":
    return 13
  if carta[0] == "Q":
    return 12
  if carta[0] == "J":
    return 11
  return (int(carta[:-1]))#:-1 vai retornar a str sem o ultimo objeto

#all verifica se todos os retornos são thrue e se forem retorna thrue
#funcao para verificar se é flush
def flush(mao):

  return all([naipe(carta) == naipe(mao[0]) for carta in mao[1:]])



#funcao para verificar fullhouse
def fullhouse(mao):
  auxi=0
  auxi2=[]
  for carta in mao:
    if valor(mao[0]) == valor(carta):
      auxi+=1
    else:
        auxi2.append(valor(carta))
  if auxi == 2:
    if auxi2[0] == auxi2[1] == auxi2[2]:
      return(True)
    else:
      return(False)
  if auxi == 3:
    if auxi2[0]==auxi2[1]:
      return(True)
    else:
      return(False)
  else:
    return(False)

#função para verificar four of a kind
def four_of(mao):
  auxi=0
  auxi_2=0
  if (valor(mao[0])==valor(mao[1])) or (valor(mao[1])==valor(mao[2])):
    for carta in mao:
      
      if valor(mao[0])==valor(carta):
        auxi+=1
      if valor(mao[1])==valor(carta):
        auxi_2+=1
      if auxi==4 or auxi_2==4:
        return(True)
      
  return(False)  

#função para verificar se é straight flush
def straight_flush(mao):
  auxi=[]
  if all([naipe(carta) == naipe(mao[0]) for carta in mao[1:]]):
    for carta in mao:
      auxi.append(valor(carta))
    auxi.sort()
    C=[]
    for i in range(len(mao) - 1):
      if auxi[i] == auxi[i + 1] - 1:
        C.append(auxi[i])
        C.append(auxi[i + 1])
        if len(C)==8:
          return(True)
      else:
        return(False)
  else:
    return(False)


  #Verificar se é royal flush
#verificar se é royal
def royal_flush(mao):
  auxi=[]
  if all([naipe(carta) == naipe(mao[0]) for carta in mao[1:]]):
    for carta in mao:
      auxi.append(valor(carta))
    auxi.sort()
    C=[]
    for i in range(len(mao) - 1):
      if auxi[i] == auxi[i + 1] - 1:
        C.append(auxi[i])
        C.append(auxi[i + 1])
        if auxi[0] == 10:
          if len(C)==8:
            return(True)
        
      else:
          return(False)
  else:
    return(False)
def straight(mao):
  auxi=[]
  for carta in mao:
    auxi.append(valor(carta))
  auxi.sort()
  C=[]
  for i in range(len(mao) - 1):
    if auxi[i] == auxi[i + 1] - 1:
      C.append(auxi[i])
      C.append(auxi[i + 1])
      if len(C)==8:
        return(True)
    else:
      return(False)
  else:
    return(False)

def three_of(mao):
  auxi=0
  auxi_2=0
  if (valor(mao[0])==valor(mao[1])) or (valor(mao[1])==valor(mao[2])):
    for carta in mao:
      
      if valor(mao[0])==valor(carta):
        auxi+=1
      if valor(mao[1])==valor(carta):
        auxi_2+=1
    if auxi==3 or auxi_2==3:
      return(True)
      
  return(False)  

def two_pair(mao):
  auxi=0
  auxi_2=0
  for x in range(len(mao)):
    for carta in mao[1:]:
      if valor(mao[x])==valor(carta):
        auxi+=1
    if auxi==2:
      auxi_2+=1
    auxi=0
  if auxi_2==2:
    return(True)
  else:
    return(False)  

def pair(mao):
  auxi=0
  for x in range(len(mao)):
    for carta in mao[:x]:
      if valor(mao[x])==valor(carta):
        auxi+=1
  if auxi==1:
    return(True)
  return(False)



  

    


      