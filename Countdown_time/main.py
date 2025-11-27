import time
from tkinter import *
window=Tk()
window.title('Countdown Time')
window.minsize(1200,1000)
def Countdown():
    select_time=int(input("Enter the time in seconds: "))

    for i in range(select_time,0,-1):
        seconds=i % 60
        mınutes=int(i/60)%60
        hours=int(i / 3600)
        print(f'{hours:02}:{mınutes:02}:{seconds:02}')
        time.sleep(1)
    print("TİME'S UP!!!")

lbl_time=Label(text="Hello")
lbl_time.grid(row=3,column=3)

window.mainloop()
