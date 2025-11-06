print("*" *35)
print("***Bem-vindo(a) ao jogo da Forca!**")
print("*" *35)

palavra_secreta = "laranja"
letras_acretadas = ['_','_','_','_','_','_','_']

enforcou = False
acertou = False
erros = 0

while(not acertou and not enforcou):
    chute = input("Qual letra deseja adicionar?")

    if(chute in palavra_secreta):
        posicao = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acretadas[posicao] = letra
            posicao = posicao + 1
    else:
        erros += 1
    enforcou = erros == 6 #se o nº de erros for igual a 7, enforcou sera True
    acertou = '_' not in letras_acretadas
    print(letras_acretadas)
if acertou:
    print("Você ganhou")
else:
    print("Você perdeu")

print("fim do jogo")