# import pyautogui as pg
# import time
# while True:
# 	a = pg.confirm("Are you chutiya !!", buttons=["yes","nope"])
# 	if a == "yes":
# 		break



# import random
# import pyautogui as pg
# import time
# words=('dumb','donkey','idiot')
# time.sleep(8)

# for i in range(100):
# 	a=random.choice(words)
# 	pg.write("you are a"+a)
# 	pg.press('enter')




# from turtle import *
# import time
#
# right(90)
# forward(200)
# left(90)
# forward(40)
# left(90)
# time.sleep(10)



import pyautogui as pg
import time

print ("program will run 10 sec")
time.sleep(6)
for i in range(200):
 	pg.write("Hello User!")
 	time.sleep(0.2)
 	pg.press("Enter")


