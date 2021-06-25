#Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido
#quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou 
#no final do jogo.
from random import randint
v = 0
while True:
    player = int(input('Diga um valor: '))
    pc = randint(0, 11)
    total = player + pc
    type = ' '
    while type not in 'PI':
        type = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'Voçe jogou {player} e o computador {pc}.Total de {total}')
    if type == 'P':
        if total % 2 == 0:
            print('Voçe Venceu!')
            v += 1
        else:
            print('Voçe Perdeu!')
            break
        if type == 'I':
            if total % 2 == 1:
                print('Voçe Venceu!')
            else:
                print('Voçe Perdeu!')
                break
    print('Vamos jogar novamente...')
print(f'GAME OVER!Voçe venceu {v} vezer')
        




  



