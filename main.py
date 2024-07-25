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

import random;

colors = ["vermelho","azul","amarelo","verde"]
reply = []
#O "Randomizador" de cores
def bot(i=2):
    selection_for_bot = []
    while i > 0:
        choose_bot = random.randint(0,3)
        bot = colors[choose_bot]
        selection_for_bot.append(bot)
        print(bot)
        i-=1
    return selection_for_bot
        

choose = bot()  
print(choose)

def verified_reply():
#Receber a resposta do usuario
    global win 
    global defeat 
    for _ in range(len(choose)):
        player = input(str("Quais foram as cores dadas pelo robo?"))
        reply.append(player)
#Verificar a resposta
    if reply == choose:
        win += 1
        return "Acertou"
    defeat +=1 
    return "Errou" 
resultado = verified_reply()
print(resultado)
#Marcador de Vitoria e derrota


