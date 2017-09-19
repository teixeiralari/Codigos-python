alfa = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
soma = 0
word = input()
for i in range(len(word)):
     soma = alfa.index(word[i]) + soma + 1
print (soma)
