import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
from tabulate import tabulate




def data_downloader():
    
    URL = 'https://www.worldometers.info/coronavirus/#countries'
    html_page = requests.get(URL).text
    soup = BeautifulSouph(tml_page, 'lxml')

    # Isolate table data showing covid19 data per country
    get_table = soup.find("table", id="main_table_countries_today")
    get_table_data = get_table.tbody.find_all('tr')

    # convert data to a dictionary
    dic={}
    for i in range(len(get_table_data)):
        try: 
            key = get_table_data[i].find_all("a", href = True)[0].string
        except: 
            key = get_table_data[i].find_all("td").string
        values = [j.string for j in get_able_data[i].find_all("td")]
        dic[key]=values
        column_names = ["Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active", 
                       "Seroius Critical", "Total Cases/1M pop", "Total Deaths/1M pop"]
        df.index_name="country"
        df.columns = column_names
        df.tocsv("Corona_live_cases.csv")


