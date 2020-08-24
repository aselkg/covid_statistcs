import requests 
import pandas as pd
response = requests.get("https://en.m.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory")

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
soup.prettify()
title = soup.title.text
# print(title)

table= soup.find('table', attrs={"class" : "wikitable"})
Country = []
Cases = []
Deaths = []
Recoveries = []
thead = table.select("tr", attrs={"class" : "sorttop"})[1]
tds = thead.find_all("th")
Country.append("World")
Cases.append(tds[2].text.replace("\n", "").strip())
Deaths.append(tds[3].text.replace("\n", "").strip())
Recoveries.append(tds[4].text.replace("\n", "").strip())

# print(thead)  

trs = table.select("tbody tr")[2:230]
for tr in trs:
    Country.append(tr.find_all("th", attrs = {'scope' : 'row'})[1].find('a').text) 
    
    tds = tr.find_all("td")
    print(len(tds))
    Cases.append(tds[0].text.replace("\n", "").strip())
    Deaths.append(tds[1].text.replace("\n", "").strip())
    Recoveries.append(tds[2].text.replace("\n", "").strip())


data = list(zip(Country, Cases, Deaths, Recoveries))
COVID_data = pd.DataFrame(data, columns=['Country', 'Cases', 'Deaths', 'Recoveries'])
COVID_data.head(10)
html = COVID_data.to_html()
text_file = open("table.html", "w")
text_file.write(html)
text_file.close()