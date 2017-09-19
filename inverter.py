answer = input("Digite uma palavra ou numero: ")
final = ''
i=0
answer=answer.split()
for letra in answer:
     final = final + (letra[::-1])
     if (i != len(answer)):
         final = (final + ' ')
         i= i+1
print (final)
