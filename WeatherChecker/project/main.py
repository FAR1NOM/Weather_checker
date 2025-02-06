from tkinter import *
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from io import BytesIO
from tkvideo import tkvideo

root = Tk()

def get_weather():
    city = cityField.get()
    key = 'YOUR_KEY'
    url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': key, 'q': city, 'units': 'metric'}
    result = requests.get(url, params=params)
    weather = result.json()

    weather_text = f'{str(weather["name"])}: {weather["main"]["temp"]}°C, {weather["weather"][0]["description"]}'
    animate_text(info, weather_text)

    # Отображение иконки погоды
    weather_icon_code = weather["weather"][0]["icon"]
    icon_url = f'http://openweathermap.org/img/wn/{weather_icon_code}@2x.png'
    icon_response = requests.get(icon_url)
    icon_image = Image.open(BytesIO(icon_response.content))
    icon_photo = ImageTk.PhotoImage(icon_image)

    weather_icon_label.config(image=icon_photo)
    weather_icon_label.image = icon_photo

def animate_text(widget, text, delay=100):
    widget.config(text="")
    def display_char(index=0):
        if index < len(text):
            widget.config(text=widget.cget("text") + text[index])
            root.after(delay, display_char, index + 1)
    display_char()

root.title('Погодное приложение')
root.geometry('700x600')
root.state('zoomed')
root.resizable(width=False, height=False)

# Настройка видеофона
video_label = Label(root)
video_label.place(relwidth=1, relheight=1)
player = tkvideo("c633c20ede82f0e0ced7d570dbe3a1f3.gif", video_label, loop=1, size=(1920, 1080))
player.play()

# Создание полупрозрачного изображения
def create_transparent_image(width, height, opacity):
    image = Image.new('RGBA', (width, height), (0, 0, 0, int(255 * opacity)))
    return ImageTk.PhotoImage(image)

# Создание полупрозрачных фреймов
transparent_image_top = create_transparent_image(1920, 108, 0.5)
transparent_image_bottom = create_transparent_image(1920, 200, 0.5)  # Увеличили высоту до 200

canvas_top = Canvas(root, bd=0, highlightthickness=0)
canvas_top.place(relx=0.5, rely=0.2, anchor=N, relwidth=0.75, relheight=0.15)
canvas_top.create_image(0, 0, image=transparent_image_top, anchor=NW)

canvas_bottom = Canvas(root, bd=0, highlightthickness=0)
canvas_bottom.place(relx=0.5, rely=0.55, anchor=N, relwidth=0.75, relheight=0.3)  # Увеличили высоту до 0.3
canvas_bottom.create_image(0, 0, image=transparent_image_bottom, anchor=NW)

frame_top = Frame(canvas_top, bg='black')
frame_top.pack(fill=BOTH, expand=True, padx=5, pady=5)

frame_bottom = Frame(canvas_bottom, bg='black')
frame_bottom.pack(fill=BOTH, expand=True, padx=5, pady=5)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12), padding=10)
style.configure('TEntry', font=('Helvetica', 12), padding=10)
style.configure('TLabel', font=('Helvetica', 12), background='black', foreground='white')

cityField = ttk.Entry(frame_top, style='TEntry')
cityField.pack(pady=10)

btn = ttk.Button(frame_top, text='Посмотреть погоду', command=get_weather, style='TButton')
btn.pack(pady=10)

info = ttk.Label(frame_bottom, text='Погодная информация', style='TLabel')
info.pack(pady=10)

weather_icon_label = ttk.Label(frame_bottom)
weather_icon_label.pack(pady=10)

root.mainloop()
