import requests 
import pandas as pd
response = requests.get("https://en.m.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory")

from bs4 import BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')
soup.prettify()
title = soup.title.text
# print(title)

section= soup.find('section', attrs={"class" : "mf-section-2"})
# print(section)
Region = []
TotalCases = []
TotalDeaths = []
CasePerMillion = []
DeathsPerMillion = []
Population = []


trs = section.select("tbody tr")[2:14]
for tr in trs:
    Region.append(tr.find_all("th", attrs = {'scope' : 'row'})[0].text) 
    
    tds = tr.find_all("td")
    # print(len(tds))
    TotalCases.append(tds[0].text.replace("\n", "").strip())
    TotalDeaths.append(tds[1].text.replace("\n", "").strip())
    CasePerMillion.append(tds[2].text.replace("\n", "").strip())
    DeathsPerMillion.append(tds[3].text.replace("\n", "").strip())
    Population.append(tds[4].text.replace("\n", "").strip())


data = list(zip(Region, TotalCases, TotalDeaths, CasePerMillion, DeathsPerMillion, Population))
COVID_data = pd.DataFrame(data, columns=['Region', 'Total Cases', 'Total Deaths', 'Case per million', 'Deaths per million', 'Population'])
COVID_data.head(10)
html = COVID_data.to_html()
text_file = open("region.html", "w")
text_file.write(html)
text_file.close()