import requests 
import pandas as pd
import re
response = requests.get("https://en.m.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States")

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
soup.prettify()
print(soup.title.text)

table= soup.find('table', attrs={"class" : "wikitable"})
State = []
Cases = []
Deaths = []
Recoveries = []
Hospitalization = []

thead = table.select("tr", attrs={"class" : "sorttop"})[2]
# print(thead)
tds = thead.find_all("th")
# print(tds)
State.append("Total")
Cases.append(tds[1].text.replace("\n", "").strip())
Deaths.append(tds[2].text.replace("\n", "").strip())
Recoveries.append(tds[3].text.replace("\n", "").strip())
Hospitalization.append(tds[4].text.replace("\n", "").strip())
trs = table.select("tbody tr")[2]



trs = table.select("tbody tr")[3:59]
for tr in trs:
    State.append(tr.find_all("th", attrs = {'scope' : 'row'})[1].find('a').text) 
    tds = tr.find_all("td")
    # print(tds)
    Cases.append(tds[1].text.replace("\n", "").strip())
    Deaths.append(tds[2].text.replace("\n", "").strip())
    Recoveries.append(tds[3].text.replace("\n", "").strip())
    Hospitalization.append(tds[4].text.replace("\n", "").strip())


data = list(zip( State, Cases, Deaths, Recoveries, Hospitalization))
COVID_data = pd.DataFrame(data, columns=['State', 'Cases', 'Deaths', 'Recoveries', 'Hospitalization'])
COVID_data.head(10)
html = COVID_data.to_html()
text_file = open("usa.html", "w")
text_file.write(html)
text_file.close()