import pyautogui as pg
import time 
import os

TAMANHO_DA_TELA = pg.size()

art = r""" 
                                                                                                                     
,--.  ,--. ,---.                                                                                                     
|  '--'  |'   .-'  ,---.  ,--,--.,--,--,--.                                                                          
|  .--.  |`.  `-. | .-. |' ,-.  ||        |                                                                          
|  |  |  |.-'    || '-' '\ '-'  ||  |  |  |                                                                          
`--'  `--'`-----' |  |-'  `--`--'`--`--`--'                                                                          
                  `--'                                                                                               
  ,---.      ,--. ,--.        ,--.                                      ,--.     ,---.                               
 /  O  \     |  | |  |,--,--, `--',--.  ,--.,---. ,--.--. ,---.  ,--,--.|  |    '   .-'  ,---.  ,--,--.,--,--,--.    
|  .-.  |    |  | |  ||      \,--. \  `'  /| .-. :|  .--'(  .-' ' ,-.  ||  |    `.  `-. | .-. |' ,-.  ||        |    
|  | |  |    '  '-'  '|  ||  ||  |  \    / \   --.|  |   .-'  `)\ '-'  ||  |    .-'    || '-' '\ '-'  ||  |  |  |    
`--' `--'     `-----' `--''--'`--'   `--'   `----'`--'   `----'  `--`--'`--'    `-----' |  |-'  `--`--'`--`--`--'    
                                                                                        `--'                                By hcast7


"""

print(art)

time.sleep(3)

os.system("cls ")
os.system("title HSpam 💬 - A Universal Spammer for any chat application - By hcast7") 

warning = r"""
HSpam, a Universal Spammer for any chat application.

This program was made for spam testing and educational use, do not use it unethically or to harm anyone

Questions and answers

Does HSpam work on any application/website?
- Yes, in most applications/websites

Is HSpam an illegal program?
- It depends on the way and version you are using, if you are using a modified version for another purpose or using the program in an unethical way, you may be punished by the application/website or service

Thank you for choosing and using HSpam!
"""
print(warning)

msgtotal = input("Enter how many times you will spam or enter X for cancel: ")
if msgtotal == "X":
    exit()
MSG_TOTAL = int(msgtotal)
enterposition = input("Go to the typing bar where you will send the messages and press Enter: ")
X = pg.position().x
Y = pg.position().y

pg.moveTo(X, Y, 0.2)   # moves mouse to X of 100, Y of 200.


print(f"The screen size is: {TAMANHO_DA_TELA.width} x {TAMANHO_DA_TELA.height}")


pg.click()

while MSG_TOTAL > 0:
    pg.write("SPAM TEST")
    pg.press("enter")
    MSG_TOTAL -= 1
