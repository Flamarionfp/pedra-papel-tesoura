from random import choice
print('-'*30)
print('Pedra Papel Tesoura'.center(30))
print('-'*30)
resposta = 'S'
resultado = ''
while resposta == 'S':
    escolhas = ['pedra', 'papel', 'tesoura']
    pc = choice(escolhas)
    jogador = str(input('Qual sua jogada? ')).lower().strip()
    while jogador != 'pedra' and jogador != 'papel' and jogador != 'tesoura':
        print('Jogada inválida!')
        jogador = str(input('Qual sua jogada? ')).lower().strip()
    print('Computador jogou {}'.format(pc.upper()))
    print('Você jogou {}'.format(jogador.upper()))
    # Formas do jogador vencer:
    if jogador == 'pedra' and pc == 'tesoura' or jogador == 'papel' and pc == 'pedra' or jogador == 'tesoura' and pc == 'papel':
        print('Você Venceu!')
    #Formas do pc vencer:
    else:
        if pc == 'pedra' and jogador == 'tesoura' or pc == 'papel' and jogador == 'pedra' or pc == 'tesoura' and jogador == 'papel':
            print('Você perdeu!')
        else:
            print('Empatou!')
    resposta = str(input('Jogar novamente (S/N)? ')).upper().strip()
    while resposta != 'S' and resposta != 'N':
        print('Resposta inválida!')
        resposta = str(input('Gostaria de jogar novamente (S/N)? ')).upper().strip()


