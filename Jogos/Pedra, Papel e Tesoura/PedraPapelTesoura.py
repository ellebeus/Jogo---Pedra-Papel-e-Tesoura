import random
def play():
    user = input("Qual a sua escolha? 'r' para pedra, 'p' para papel, 't' para tesoura\n")
    if user not in ['r', 'p', 't']:
        return "Escolha inválida. Tente novamente."

    computer = random.choice(['r', 'p', 't'])

    if user == computer:
        print("O computador escolheu {}!".format(computer))
        return 'Empate!'

    if is_win(user, computer):
        print("O computador escolheu {}!".format(computer))
        return 'Você ganhou!'

    print("O computador escolheu {}!".format(computer))
    return 'Você perdeu!'
def is_win(player, opponent):
    if (player == 'r' and opponent == 't') or (player == 't' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

print(play())
