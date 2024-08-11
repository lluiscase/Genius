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
import time
difficulty = 1
defeat = -1
win = 0

#Cores usadas no jogo
colors = ["vermelho","azul","amarelo","verde"]
#Criando uma lista para receber as resposta do usuário
reply = []

#O jogo só acabará se defeat chegar a 0 (valor inicial é -1)
while defeat < 0:
#Função que cria uma lista onde armazenará as cores
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
        time.sleep(1.5)
        #Apagará a linha que mostra a cor, tendo exatos 1.5 segundos para o usuario guardar a resposta
        print("\033[A\033[K", end="")
        

    def verified_reply():
        global difficulty
        global defeat
        global win
    #Recebe a resposta do usuario
        print("Responda de acordo com o que foi mostrado (por ordem)")
        for _ in range(len(choose)):
            player = input(str())
            reply.append(player)
    #Verificar a resposta
        if reply != choose:
            defeat += 1
            return "Perdeu"
        difficulty += 1
        win += 1
        return "Acertou"
    resultado = verified_reply()
    print("Acertos atual: {}, Dificuldade atual: {}".format(win,difficulty))
    print(resultado)
    reply.clear()


