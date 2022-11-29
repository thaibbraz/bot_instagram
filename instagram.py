import pyautogui as pg
import keyboard as key
import time
import random

print(pg.position())
# time.sleep(3)
# # print(pg.position())

# Buscador
pg.leftClick(37, 266)      
time.sleep(1)
key.write("#pythoncode")    
time.sleep(2)

# Clicar na primeira opção
pg.leftClick(283, 279)
time.sleep(3)

# Clicar na primeira foto
pg.leftClick(821, 555)
time.sleep(3)

lista = ["Otimo conteudo!", "Incrivel :)","Demais 🔥"]

for i in range(5):
    #Dar like na foto
    pg.doubleClick(702, 662)
    time.sleep(1)

    #Deixar comentário
    pg.leftClick(1249, 935)
    msg = random.choice(list)
    pg.typewrite(msg)
    time.sleep(1)
    pg.press("enter")
    time.sleep(6)

    #Próximo
    pg.leftClick(1872, 521)
    time.sleep(3)

