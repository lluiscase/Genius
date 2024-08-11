'''Esse projeto consiste na criação de um jogo baseado no GENIUS
Uma cor irá piscar e apagará varias vezes em uma sequencia na qual o jogador deverá acertar
O que deve ter no codigo:
- Marcador de Vitoria e derrota
- Interface(futuramente)
- o "Randomizador" de cores
- Dificuldade aumentando conforme acertos
- Adicionar uma musica 8-bit(futuramente)?# Genius
-Receber a resposta do usuario
- verificação da resposta
- Loop
# Genius'''

import random
difficulty = 1
defeat = -1
win = 0

colors = ["vermelho","azul","amarelo","verde"]
reply = []

while defeat < 0:
#O "Randomizador" de cores
    def bot(i=difficulty):
        selection_for_bot = []
        while i > 0:
            choose_bot = random.randint(0,3)
            bot = colors[choose_bot]
            selection_for_bot.append(bot)
            i-=1
        return selection_for_bot

    choose = bot()
    for _ in range(len(choose)):
        print("Piscou: {}".format(choose[_]))
        

    def verified_reply():
        global difficulty
        global defeat
        global win
    #Receber a resposta do usuario
        for _ in range(len(choose)):
            player = input(str("Quais foram as cores dadas pelo robo?"))
            reply.append(player)
    #Verificar a resposta
        reply == choose and (difficulty := difficulty + 1, win := win + 1) or (defeat := defeat + 1)
        return "Acertou" if reply == choose else "Perdeu"
    resultado = verified_reply()
    print("Acertos atual: {}".format(win))
    print("Dificuldade atual: {}".format(difficulty))
    print(resultado)
    reply.clear()
    



