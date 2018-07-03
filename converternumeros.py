#Converter numero decimal para binario e vice-versa
#converter numero decimal para hexadecimal e vice-versa

def singlenumber(numList):# [1,2,3]
    
    s = map(str, numList)   # ['1','2','3']
    s = ''.join(s)          # '123'
    return s

def d2b(number):
    conversao = []
    quoc = 2
    while(quoc != 1):
        quoc = number // 2
        resto = number % 2
        number = quoc
        conversao.append(resto)
    conversao.append(quoc)
    conversao = singlenumber(conversao[::-1])
    return conversao

def b2d(number):
    i = len(number)
    dec = 0
    for dig in number:
        i -= 1
        dec += int(dig) * (2**i)
    return dec

def d2h(number):
    conversao = []
    quoc = 1
    while(quoc != 0):
        quoc = number // 16
        resto = number % 16
        number = quoc
        if resto > 9:
            resto = chr(resto + 55)
            conversao.append(resto)
        else:
            conversao.append(resto)
    conversao = singlenumber(conversao[::-1])
    return conversao

def h2d(number):
    i = len(number)
    hexa = 0
    for dig in number:
        i -= 1
        if dig.isdigit():
            hexa += int(dig) * (16**i)
        else:
            hexa += (ord(dig) - 55) * (16 ** i)
    return hexa
        
    
opt = 'S'    
while(opt == 'S'):
    print('------------------ MENU -----------------------\n')
    print('1 - Decimal para binário\n2 - Binário para decimal')
    print('3 - Decimal para hexadecimal\n4 - Hexadecimal para binário')
    print('\nDigite uma opção: ')
    escolha = int(input())
    print('\nInsira o número que deseja converter: ')
    number = input().upper()
    if escolha == 1:
        print('\nO número em binário é: ',d2b(int(number)))
    elif escolha == 2:
        print('\nO número em decimal é: ', b2d(number))
    elif escolha == 3:
        print('\nO número em hexadecimal é: ', d2h(int(number)))
    elif escolha == 4:
        print('\nO número em decimal é: ', h2d(number))
    else:
        print('\nOpção inválida')
    print('\nDeseja continuar? (S/N)')
    opt = input().upper()


