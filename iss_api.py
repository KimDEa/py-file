import requests
import json
from tkinter import *
from datetime import datetime

window = Tk()
window.title("ISS Tracking Info.")
window.config(padx=15, pady=15)

def update():
    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()
    data_iss_latitude = response_iss.json()["iss_position"]["latitude"]
    data_iss_longitude = response_iss.json()["iss_position"]["longitude"]
    data_iss_timestamp = response_iss.json()["timestamp"]
    date_object = datetime.fromtimestamp(data_iss_timestamp)

    my_lat = (37.45463062487527)
    my_lng = (126.6538276912455)

    parameters = {
        "lat": my_lat,
        "lng": my_lng,
        "time_format": "iso8601"
    }

    response_latlong = requests.get(url="https://api.sunrise-sunset.org/v2", params=parameters)
    response_latlong.raise_for_status()
    data_latlong = response_latlong.json()

    iss_lat_diff = int(data_iss_latitude.split(".")[0])
    iss_lng_diff = int(data_iss_longitude.split(".")[0])
    my_lat_diff = int(data_latlong["lat".split(".")[0]])
    my_lng_diff = int(data_latlong["lng".split(".")[0]])

    if iss_lat_diff < my_lat_diff + 5 and iss_lat_diff > my_lat_diff - 5 or iss_lat_diff == my_lat_diff:
        new_window = Tk()
        new_window.config(padx=15, pady=15)
        head = Label(new_window, text="ISS is above your head right now.", font=('Arial', 15))
        head.grid(row=0, column=0, columnspan=3)

    iss_lat = Label(text=f"ISS latitude: {data_iss_latitude}.")
    iss_lat.grid(row=0, column=0, columnspan=3)

    iss_lng = Label(text=f"ISS longitude: {data_iss_longitude}.")
    iss_lng.grid(row=1, column=0, columnspan=3)

    iss_time = Label(text=f"timestamp: {date_object.strftime("%Y-%m-%d %H:%M:%S")}.")
    iss_time.grid(row=2, column=0, columnspan=3)

    latlong_tzid = Label(text=f"tzid: {data_latlong["tzid"]}.")
    latlong_tzid.grid(row=4, column=0, columnspan=3)
    latlong_utc_offset = Label(text=f"utc_offset: {data_latlong["utc_offset"]}.")
    latlong_utc_offset.grid(row=5, column=0, columnspan=3)
    latlong_my_lat = Label(text=f"current latitude: {data_latlong["lat"]}.")
    latlong_my_lat.grid(row=6, column=0, columnspan=3)
    latlong_my_lng = Label(text=f"current longitude: {data_latlong["lng"]}.")
    latlong_my_lng.grid(row=7, column=0, columnspan=3)
    latlong_sunrise = Label(text=f"sunrise: {data_latlong["sunrise"]}.")
    latlong_sunrise.grid(row=8, column=0, columnspan=3)
    latlong_sunset = Label(text=f"sunset: {data_latlong["sunset"]}.")
    latlong_sunset.grid(row=9, column=0, columnspan=3)
    latlong_sun_status = Label(text=f"sun_status: {data_latlong["sun_status"]}.")
    latlong_sun_status.grid(row=10, column=0, columnspan=3)
    latlong_moon_phase = Label(text=f"moon_phase: {data_latlong["moon_phase"]}.")
    latlong_moon_phase.grid(row=11, column=0, columnspan=3)
    latlong_moon_illum = Label(text=f"moon_illumination: {data_latlong["moon_illumination"]}.")
    latlong_moon_illum.grid(row=12, column=0, columnspan=3)

    window.after(60000, update)

update()

window.mainloop()