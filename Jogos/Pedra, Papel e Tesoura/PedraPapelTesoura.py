import random
def play():
    user = input("Qual a sua escolha? 'pedra', 'papel', 'tesoura'\n")
    if user not in ['pedra', 'papel', 'tesoura']:
        return "Escolha inválida. Tente novamente."

    computer = random.choice(['pedra', 'papel', 'tesoura'])

    if user == computer:
        print("O computador escolheu {}!".format(computer))
        return 'Empate!'

    if is_win(user, computer):
        print("O computador escolheu {}!".format(computer))
        return 'Você ganhou!'

    print("O computador escolheu {}!".format(computer))
    return 'Você perdeu!'
def is_win(player, opponent):
    if (player == 'pedra' and opponent == 'tesoura') or (player == 'tesoura' and opponent == 'papel') \
        or (player == 'papel' and opponent == 'pedra'):
        return True

print(play())
