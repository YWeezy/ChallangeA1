woorden = ["pepper","playboy","billionare"]

def check(letter ,woord):
  listret = []
  for l in range(len(woord)):
    
    if letter == woord[l]:
      listret.append(l)

  if not listret:
    return "none"
  else:
    return listret




def gal(woorden):
  for i in range(2):
    
    word = woorden[i]
    pogingen = 7
    while pogingen < 1:
    
      lettinp = input("Vul een letter in")
      print(check(lettinp, word)
