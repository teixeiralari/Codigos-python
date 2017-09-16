def pig():
  pyg = 'ay'
  answer = input("Digite uma palavra em ingles: ")
  if len(answer)>0 and answer.isalpha():
    word = answer.lower()
    print (word[1:len(word)] + word[0] + pyg)
    resp = input("Deseja continuar S/N?")
    if resp == "S" or "s":
      pig()
pig()
