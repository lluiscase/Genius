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
# Genius'''

import random;

colors = ["vermelho","azul","amarelo","verde"]
y=0
reply = []
#O "Randomizador" de cores
def bot(i=2):
    selection_for_bot = []
    x=0
    while i > x:
        choose_bot = random.randint(0,3)
        bot = colors[choose_bot]
        selection_for_bot.append(bot)
        print(bot)
        i-=1
    return selection_for_bot
        

#Receber a resposta do usuario
choose = bot()  
print(choose)
while len(choose) > y:
    player = input(str(print("Quais foram as cores dadas pelo robo?")))
    reply.append(player)
    y +=1

print(reply)
#Verificar a resposta
#Marcador de Vitoria e derrota
