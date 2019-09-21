import random
escolhas = ('Pedra', 'Papel', 'Tesoura')
print('Vamos jogar Jokenpô')
print('Escolha:\n[ 0 ] PEDRA\n[ 1 ] PAPEL\n[ 2 ] TESOURA')
player = int(input())
ia = random.randint(0, 2)
if player == 0:
    if ia == 2:
        print('Você escolheu {} e seu oponente escolheu {}.\nParabéns, você venceu'.format(escolhas[player], escolhas[ia]))
    if ia == 1:
        print('Você escolheu {} e seu oponente escolheu {}.\nVocê Perdeu'.format(escolhas[player], escolhas[ia]))
    if ia == 0:
        print('Você escolheu {} e seu oponente escolheu {}.\nVocês Empataram'.format(escolhas[player], escolhas[ia]))
elif player == 1:
    if ia == 2:
        print('Você escolheu {} e seu oponente escolheu {}.\nVocê Perdeu.'.format(escolhas[player], escolhas[ia]))
    if ia == 1:
        print('Você escolheu {} e seu oponente escolheu {}.\nVocês Empataram'.format(escolhas[player], escolhas[ia]))
    if ia == 0:
        print('Você escolheu {} e seu oponente escolheu {}.\nParabéns, você Venceu'.format(escolhas[player], escolhas[ia]))
elif player == 2:
    if ia == 2:
        print('Você escolheu {} e seu oponente escolheu {}.\nVocês Empataram'.format(escolhas[player], escolhas[ia]))
    if ia == 1:
        print('Você escolheu {} e seu oponente escolheu {}. \nParabéns, você Venceu'.format(escolhas[player], escolhas[ia]))
    if ia == 0:
        print('Você escolheu {} e seu oponente escolheu {}.\nVocê perdeu.'.format(escolhas[player], escolhas[ia]))