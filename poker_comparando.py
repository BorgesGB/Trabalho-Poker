#comparar duas maos, primeiro colocar em ordem de prioridade as funções de comparação
#Paus__P 0.4
#Espadas__E 0.3
#Copas__C 0.2
#Ouros__O 0.1
#EXEMPLO DE FORMATAÇÃO DE MAO A SER SEGUIDO:["AC", "05P", "10C", "07O", "03E"]
mao1=["AC", "06O", "06C", "06O", "03E"]
mao2=["2C", "05P", "10C", "07O", "03E"]
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

def grnipe(carta):
  if naipe(carta)=="O":
      pontosn=0.1
  if naipe(carta)=="C":
    pontosn=0.2
  if naipe(carta)=="E":
    pontosn=0.3
  if naipe(carta)=="P":
    pontosn=0.4
  return(pontosn)

#separa cada patamar de mao por um numero, caso sejam iguai
def graduacao(mao):
  if royal_flush(mao):
    return(10)
  if straight_flush(mao):
    return(9)
  if four_of(mao):
    return(8)
  if fullhouse(mao):
    return(7)
  if flush(mao):
    return(6)
  if straight(mao):
    return(5)
  if three_of(mao):
    return(4)
  if two_pair(mao):
    return(3)
  if pair(mao):
    return(2)
  else:
    return(1)

def comparar(mao1, mao2):
  pontos1=graduacao(mao1)
  pontos2=graduacao(mao2)
  if pontos1==pontos2:
    
    if pontos1==9:  
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      for x in len(mao1)[1:]:
        if a1[-x]>b2[-x]:
            return(mao1)
        if a1[-x]<b2[-x]:
            return(mao2)
    if pontos1==8:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      if a1[1]>b2[1]:
        return(mao1)
      if a1[1]<b2[1]:
        return(mao2)
    if pontos1==7:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      if a1[2]>b2[2]:
        return(mao1)
      if a1[2]<b2[2]:
        return(mao2) 
    if pontos1==6:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      for x in len(mao1)[1:]:
        if a1[-x]>b2[-x]:
            return(mao1)
        if a1[-x]<b2[-x]:
            return(mao2)
    if pontos1==5:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      if a1[-1]>b2[-1]:
        return(mao1)
      if a1[-1]<b2[-1]:
        return(mao2)
    if pontos1==4:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      if a1[2]>b2[2]:
        return(mao1)
      if a1[2]<b2[2]:
        return(mao2)
    if pontos1==3:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      if a1[3]>b2[3]:
        return(mao1)
      if a1[3]<b2[3]:
        return(mao2)
    if pontos1==2:
      a1=[]
      b2=[]
      a2=[]
      b1=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      for x in range(4):
        if a1[x]==a1[x+1]:
          a2.append(a1[x])
        if b2[x]==b2[x+1]:
          b1.append(b2[x])
      if a2[0]>b1[0]:
        return(mao1)
      if a2[0]<b1[0]:
        return(mao2)
    if pontos1==1:
      a1=[]
      b2=[]
      for carta in mao1:
        a1.append(valor(carta))
      for carta in mao2:
        b2.append(valor(carta))
      a1=sorted(a1)
      b2=sorted(b2)
      if a1[-1]>b2[-1]:
        return(mao1)
      if a1[-1]<b2[-1]:
        return(mao2)

  elif pontos1>pontos2:
    return(mao1)
  elif pontos1<pontos2:
    return(mao2)

print(comparar(mao1, mao2))
    
  
  


  
    
    
