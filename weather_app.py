import requests
import json
import pyttsx3

engine = pyttsx3.init()
city = input("Enter the city to Check Weather: ")
url = f"https://api.weatherapi.com/v1/current.json?key=c2b24258866c4c22894145857251111&q={city}&aqi=no"
r = requests.get(url)
wdic = json.loads(r.text)
w = wdic["current"]["temp_c"]
engine.say(f"The current Weather in {city} is {w} degrees")
print(w,"Degrees")
engine.runAndWait()
engine.stop()
