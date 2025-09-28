from tkinter import *

window=Tk()
window.minsize(500,500)
window.title('Roman Numeral Converter')


def romanToInt():
    try:
        user_input=str(input_num.get())
        dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        integer=0

        for i in range(len(user_input)):
            value = dict[user_input[i]]

            if i + 1 < len(user_input) and dict[user_input[i + 1]] > value:
                integer -=value

            else:
                integer+=value

        lbl_integer=Label(text=integer,width=20,bg='green',fg='white',font=('Arial',20,'bold'))
        lbl_integer.place(x=90,y=90)

    except:
        lbl_error=Label(text='Error!',width=20,bg='green',fg='red',font=('Arial',20,'bold'))
        lbl_error.place(x=90,y=90)









lbl_enter=Label(text='Enter Rome Number')
lbl_enter.place(x=190,y=0)

input_num=Entry(width=15)
input_num.place(x=200,y=20)

show_btn=Button(text='Show',width=10,command=romanToInt)
show_btn.place(x=208,y=45)




window.mainloop()