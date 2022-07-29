# Importing Modules
from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Getting Page Using GET Method
url = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(url)

# Starting bs4 And Finding The Table
soup = bs(page.text,'html.parser')
star_table = soup.find_all('table')

# Creating A Temporary List And Finding Table Rows
temp_list= []
table_rows = star_table[7].find_all('tr')

# Putting Data in Rows
for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

# Creating Empty Arrays Of Specified Modules That Are To Be Scraped
Name = []
Distance =[]
Mass = []
Radius =[]

# Specifying Modules To Scrape
for i in range(1,len(temp_list)):    
    Name.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

    
# Printing Data into a 'data.csv' file
df2 = pd.DataFrame(list(zip(Name,Distance,Mass,Radius,)), columns=['Name','Distance','Mass','Radius'])
df2.to_csv('data.csv')
