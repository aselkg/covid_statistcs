import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Template:COVID-19_pandemic_data#covid19-container'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

countries = soup.find(id="covid19-container")
#print(countries.prettify())

country_elems = countries.find_all('tr')
#print(continent_elems)

for country_elem in country_elems:
    #print(country_elem, end='\n'*2)
    td_list = country_elem.find_all("td")
    title_elem = country_elem.find("a")
    cases_elem = country_elem.findAll('th')[0].text
    # deths_elem = td_list[1].text
    #print(title_elem)
    print(country_elem[1])
    # print(deths_elem)
    # print()
