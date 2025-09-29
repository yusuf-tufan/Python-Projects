import requests
from tkinter import *
import messagebox
from PIL import ImageTk, Image

#window
window=Tk()
window.title('Weather App')
window.state('zoomed')
window.configure(bg='light blue')
window.resizable(False,False)
#image
img=Image.open('image_weather.png')
resized=img.resize((1650,1000),Image.Resampling.LANCZOS)
itk=ImageTk.PhotoImage(resized)
lbl=Label(window,image=itk)
lbl.image=itk
lbl.pack()

# get data
def get_data():
    user_city=user_input.get()

    #get data of weather from url
    api_key = '0a4209e367094a64a8495348250507'#special key
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={user_city}&aqi=no'
    get_url = requests.get(url)

    responsew=get_url.json()

    #show weather
    if get_url.status_code==200:
        data_lbl.config(text=f'\nLocation: {responsew['location']['name']}\n'
                            f'Degree(°C): {responsew['current']['temp_c']}°C\n'
                            f'Degree(°F): {responsew['current']['temp_f']}°F\n'
                            f'Air: {responsew['current']['condition']['text']}\n'
                            f'Humidity: {responsew['current']['humidity']}%\n'
                            f'Wind(kph): {responsew['current']['wind_kph']}kph\n'
                            f'Precipitation(mm): {responsew['current']['precip_mm']}%\n'
                       )
        data_lbl.config(width=70,bg='light green',fg='black',font=('Arial',15,'italic','bold'))
        data_lbl.place(x=345,y=130)
        click_button.config(state='disabled')
        clear_btn.place(x=755,y=360)

    else:
        messagebox.showinfo(title='Error',message='Please Can You Chack Your Informations.\n'
                                                  '-Check characters of word.\n'
                                                  '-Make sure you enter the correct city.'
                            )

def clear_all():
    click_button.config(state='active')
    user_input.delete(0,END)
    data_lbl.config(text='')
    data_lbl.place(x=10000000,y=1000000000)

#Label of weather
data_lbl=Label(text='')

#Label Enter
enter_lbl=Label(text='Enter A City',bg='light green',fg='black',font=('Arial',11,'bold'))
enter_lbl.place(x=750,y=35)

#enter city
user_input=Entry(width=25,font=('Arial',10,'italic','bold'))
user_input.place(x=705,y=65)

#click button
img_search=PhotoImage(file='search.png')
img_search=img_search.subsample(7,7)
click_button=Button(image=img_search,command=get_data)
click_button.place(x=780,y=90)

#clear button
img_clear=PhotoImage(file='delete.png')
img_clear=img_clear.subsample(8,8)
clear_btn=Button(image=img_clear,command=clear_all)

window.mainloop()
