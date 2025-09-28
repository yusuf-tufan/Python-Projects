import time
import tkinter
from tkinter import *

#window
window=Tk()
window.title('Calculator App')
window.config(padx=30,pady=30)
window.minsize(600,800)

#transactions
def click_button():
    num1=enter_num1.get()
    num2=enter_num2.get()
    enter_process1=enter_process.get()

    try:
        result = int(num1),int(num2)
        lbl = Label(window, text='Please select a option.', width=40, bg='red',fg='white', font=('Arial', 15, 'italic', 'bold'))
        lbl.place(x=70, y=120)
    except:
        error_lbl = Label(window, text='')
        error_lbl.place(x=70, y=120)
        try:
            result = float(num1),float(num2)
            lbl = Label(window, text='Please select a option.', width=40, bg='red', fg='white',font=('Arial', 15, 'italic', 'bold'))
            lbl.place(x=70, y=120)
        except:
            error_lbl = Label(window, text='Please enter just number.', width=40, bg='red',fg='white', font=('Arial', 15, 'italic', 'bold'))
            error_lbl.place(x=70, y=120)

    if enter_process1=='+':
        try:
            result = int(num1) + int(num2)
            lbl = Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
            lbl.place(x=70,y=120)
        except:
            error_lbl = Label(window, text='')
            error_lbl.place(x=70, y=120)
            try:
                result = float(num1) + float(num2)
                lbl =Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
                lbl.place(x=70, y=120)
            except:
                error_lbl = Label(window, text='Please enter just number.', width=40, bg='red',fg='white', font=('Arial', 15, 'italic', 'bold'))
                error_lbl.place(x=70, y=120)

    elif enter_process1=='*':
        try:
            result = int(num1) * int(num2)
            lbl = Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
            lbl.place(x=70,y=120)
        except:
            error_lbl = Label(window, text='')
            error_lbl.place(x=70, y=120)
            try:
                result = float(num1) * float(num2)
                lbl =Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
                lbl.place(x=70, y=120)
            except:
                error_lbl = Label(window, text='Please enter just number.', width=40, bg='red',fg='white', font=('Arial', 15, 'italic', 'bold'))
                error_lbl.place(x=70, y=120)
    elif enter_process1=='-':
        try:
            result = int(num1) - int(num2)
            lbl = Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
            lbl.place(x=70,y=120)
        except:
            error_lbl = Label(window, text='')
            error_lbl.place(x=70, y=120)
            try:
                result = float(num1) - float(num2)
                lbl =Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
                lbl.place(x=70, y=120)
            except:
                error_lbl = Label(window, text='Please enter just number.', width=40, bg='red',fg='white', font=('Arial', 15, 'italic', 'bold'))
                error_lbl.place(x=70, y=120)
    elif enter_process1=='/':
        try:
            result = int(num1)/int(num2)
            lbl = Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
            lbl.place(x=70,y=120)
        except:
            error_lbl = Label(window, text='')
            error_lbl.place(x=70, y=120)
            try:
                result = float(num1)/float(num2)
                lbl =Label(window, text=result, width=40, bg='orange', font=('Arial', 15, 'italic', 'bold'))
                lbl.place(x=70, y=120)
            except:
                error_lbl = Label(window, text='Please enter just number.', width=40, bg='red',fg='white', font=('Arial', 15, 'italic', 'bold'))
                error_lbl.place(x=70, y=120)
    else:
        if len(enter_process1)>1:
            lbl = Label(window, text='Please enter one symbol.', width=40, bg='red', fg='white',font=('Arial', 15, 'italic', 'bold'))
            lbl.place(x=70, y=120)


num1_lbl=Label(text='Number:')
num1_lbl.place(x=50,y=0)
num2_lbl=Label(text='Number:')
num2_lbl.place(x=270,y=0)

#enter numbers
enter_num1=Entry(width=15)
enter_num1.place(x=50,y=25)
enter_num2=Entry(width=15)
enter_num2.place(x=270,y=25)

#Calculate
calculate_button=Button(text='Calculate',width=20,bg='light green',font=('Arial',10,'italic','bold'),command=click_button)
calculate_button.place(x=70,y=80)

#process
process_lbl=Label(text='enter\none process\n(+,*,-,/)')
process_lbl.place(x=150,y=0)
enter_process=Entry(width=2,bg='white',fg='blue',font=('Arial',20,'italic','bold'))
enter_process.place(x=220,y=20)


window.mainloop()