#for temperature
import requests
import re
from bs4 import BeautifulSoup
a = str(input("Enter the City : "))
search = ("weather in", a)
url = f"https://www.google.com/search?&q={search}"
r = requests.get(url)
s = BeautifulSoup(r.text, "html.parser")
update = s.find("div", class_="BNeawe").text
update1 = s.find("span", class_="BNeawe tAd8D AP7Wnd").text
update2 = s.find("div", class_="BNeawe tAd8D AP7Wnd").text
print(update1)
print(update2)
# degree to f
a1 = re.sub("\D", "", update)
a2 = int(a1)
a3 = float(a2*9/5)+32
a4 = u"\N{DEGREE SIGN}"
#print temperature
print("Temperature of the city : ", update , "and", a3,a4,"F")
#time and date
import datetime
now = datetime.datetime.now()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d  %H:%M:%S"))
#nxt update




