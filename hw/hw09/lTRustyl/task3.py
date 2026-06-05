import tkinter as tk
from pyowm import OWM

API_KEY = 'ef2206ff5da67de63306d0b143e20872'

# OpenWeatherMap setup
owm = OWM(API_KEY)
mgr = owm.weather_manager()

HEIGHT = 350
WIDTH = 450


def get_weather():
    city = entry_field.get()

    try:
        observation = mgr.weather_at_place(city)
        w = observation.weather

        weather_info = (
            f"City: {city}\n\n"
            f"Status: {w.detailed_status}\n"
            f"Temperature: {w.temperature('celsius')['temp']} °C\n"
            f"Humidity: {w.humidity}%\n"
            f"Clouds: {w.clouds}%\n"
            f"Wind speed: {w.wind().get('speed', 'N/A')} m/s\n"
            f"Rain: {w.rain}"
        )

        label.config(text=weather_info)

    except Exception:
        label.config(text="City not found or API error")


root = tk.Tk()
root.title("Weather Application")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="deep sky blue", bd=5)
frame.place(relx=0.5,
            rely=0.1,
            relwidth=0.75,
            relheight=0.1,
            anchor='n')

entry_field = tk.Entry(frame, font=('Courier', 12))
entry_field.place(relx=0,
                  rely=0,
                  relwidth=0.65,
                  relheight=1)

button = tk.Button(
    frame,
    text="Get Weather",
    bg="gray",
    fg="white",
    font=('Courier', 8),
    command=get_weather
)
button.place(relx=0.7,
             rely=0,
             relwidth=0.3,
             relheight=1)

lower_frame = tk.Frame(root, bg='gold', bd=10)
lower_frame.place(relx=0.5,
                  rely=0.25,
                  relwidth=0.75,
                  relheight=0.6,
                  anchor='n')

label = tk.Label(
    lower_frame,
    font=('Courier', 12),
    justify='left',
    anchor='nw'
)
label.place(relx=0,
            rely=0,
            relwidth=1,
            relheight=1)

root.mainloop()

