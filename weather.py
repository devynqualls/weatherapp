import Tkinter as tk
import requests 
import time

#Get data from API
def getWeather(canvas):
    city = textfield.get()
    api - "api.openweathermap.org/data/2.5/weather?q="+ city+"&appid=156af92f32ba09e4e0287fd07eb7ea36"
    json_data = requests.get(api).json()
    condition = json_data['weatheer'][0]['main']
    temp = int(json_data['main']['temp'] -273.15)
    temp_min = int(json_data['main']['temp_min'] -273.15)
    temp_max = int(json_data['main']['temp_max'] -273.15)
    

    final_info = condition + '\n' + str(temp) + "C"
    final_data = "\n" + "Max Temp" + str(max_temp) + "\n" + 'Min Temp'
    label1.config(text = final_info)
    label2.connfig(text = final_data)




canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")

textfield = tk.Entry(canvas)
textfield.pack(pady = 20)
textfield.focus()
textfield.bind('<return>', getWeather)

label1 = tk.Label(canvas)
label1.pack()
label2 = tk.Label(canvas)
label2.pack()

canvas.mainloop()


# api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}  
#api key = 156af92f32ba09e4e0287fd07eb7ea36
