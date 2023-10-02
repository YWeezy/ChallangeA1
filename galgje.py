


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
  pogingen = 0
  for i in range(3):
    next = True
    woord = woorden[i]
    galwoord = ""
    for s in range(len(woord)):
      galwoord += "_"
    print("WOORD: " + galwoord)
    
    pogingen = 7
    while pogingen > 0:
      lettinp = input("Vul een letter in: ")

      if lettinp == "/":
        next = False
        break

      list = check(lettinp, woord)
      if list == "none":
        pogingen -= 1
        print(pogingen)
      else:
        for a in list:
          # print(a)
          # print(galwoord[list[a]])
          # print(woord[list[a]])
          galwoord = galwoord[:a] + woord[a] + galwoord[a+1:]

          # galwoord[a].replace(woord[a])
        print("gal = " + galwoord)
      if galwoord == woord:
        break
      
    
    if pogingen < 1:
      next = False
      print("You Died")
      
    else:
      return "MARK DEADPOOL(Space travel)"
    if next == False:
      break
    

