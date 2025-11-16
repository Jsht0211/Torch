import os
import time

t = input("duration(s): ")
f = input("frequency(Hz): ")
if t == "" or f == "": exit()
t = float(t)
f = float(f)
start = time.time()
while time.time() - start < t:
    os.system("termux-torch on")
    time.sleep(1/f/2)
    os.system("termux-torch off")
    time.sleep(1/f/2)
