import requests
from tkinter import *
import messagebox
from PIL import ImageTk, Image

#window
window=Tk()
window.title('Weather App')
window.state('zoomed')
window.configure(bg='light blue')
window.resizable(False,True)
#image
img=Image.open('Weather_app/image_weather.png')
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
        data_lbl.config(text=f'\nLocation: {responsew['location']['name']}/{responsew['location']['country']}\n\n'
                            f'Degree(°C): {responsew['current']['temp_c']}°C\n\n'
                            f'Degree(°F): {responsew['current']['temp_f']}°F\n\n'
                            f'Air: {responsew['current']['condition']['text']}\n\n'
                            f'Humidity: {responsew['current']['humidity']}%\n\n'
                            f'Wind(kph): {responsew['current']['wind_kph']} kph\n\n'
                            f'Precipitation(mm): {responsew['current']['precip_mm']} mm\n\n'
                            f'Time: {responsew['location']['localtime']}\n\n',
                            
                       )
        data_lbl.config(width=50,bg='medium sea green',fg='black',font=('Arial',15,'italic','bold'))
        data_lbl.place(x=500,y=150)
        search_btn.config(state='disabled')
        clear_btn.place(x=985,y=65)

    else:
        messagebox.showinfo(title='Error',message='Please Can You Chack Your Informations.\n'
                                                  '-Check characters of word.\n'
                                                  '-Make sure you enter the correct city.'
                            )

def clear_all():
    search_btn.config(state='active')
    user_input.delete(0,END)
    data_lbl.config(text='')
    data_lbl.place(x=10000,y=10000)

#Label of weather
data_lbl=Label(text='')

#Label Enter
enter_lbl=Label(text='Enter A City',bg='medium sea green',fg='black',font=('Arial',15,'bold'))
enter_lbl.place(x=750,y=30)

#enter city
user_input=Entry(width=25,font=('Arial',15,'italic','bold'))
user_input.place(x=660,y=65)

#click button
img_search=PhotoImage(file='Weather_app/search.png')
img_search=img_search.subsample(9,9)
search_btn=Button(image=img_search,command=get_data)
search_btn.place(x=950,y=65)

#clear button
img_clear=PhotoImage(file='Weather_app/delete.png')
img_clear=img_clear.subsample(37,37)
clear_btn=Button(image=img_clear,command=clear_all,background='red')

window.mainloop()
