import requests
import json
def speak(str) :
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.speak(str)

url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=48b247d482c8403c8f84d27d047dada9"
newsss = requests.get(url).text
newsss_dict = json.loads(newsss)
heatline = newsss_dict['articles']
print("###############################/n#########################3")
speak("good morning RISHABH SIR")
for x in heatline:
    speak(x['title'])
    speak(x['description'])
    speak("Rishabh Sir  next head line is  ")

