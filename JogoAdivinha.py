# jogo do advinha
# 1 - o jogo irar definir qual numero vai ser escolhido (sortear o numero)
# 2 - usuario irar entrar com um numero tentando descobrir o numero sorteado
# 3 - jogo irar validar se aquele numero esta certo ou nao
# 4 - se ele estiver certo, irar imprimir que ele acertou e parabenizar7
# 5 - se ele errar, irar aumentar uma tentativa e irar imprimir que ele errou e mostrar o numero de tentativas que ele gastou

import random

numero_secreto = random.randint(1, 15)

tentativa = 0
tentativa_maxima = 3


def vivo(tentativa, tentativa_maxima):
    if tentativa < tentativa_maxima:
        return True
    print(f"Derrota! voce acabou usando todas as suas tentativas!")
    return False


print(f"Seja bem vindo(a), você esta no desafio! ")
print('O desafio consiste em acertar o numero que a maquina escolheu, o numero esta entre 1 a 15, e voce tem 5 tentativas')

while vivo(tentativa, tentativa_maxima):    

    print( f'Resta {tentativa_maxima - tentativa} tentativas')
    jogada_player = int (input("qual seu palpite: \n"))
    if jogada_player >= 1 and jogada_player <= 15:
        tentativa += 1
        if jogada_player == numero_secreto:
            print (f"Parabens, voce acertou!!! Voce usou {tentativa} tentativas")
            break
        elif jogada_player > numero_secreto:
            print(f"O numero secreto é menor...")
        else: 
            print(f"O numero secreto é maior... ")
    else:
        print('escolha de 1 a 15')
            