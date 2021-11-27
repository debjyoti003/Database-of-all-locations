from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://en.wikipedia.org/wiki/List_of_sovereign_states_and_dependent_territories_by_continent'
r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')
list1 = soup.findAll('td', attrs={'style': 'vertical-align:top;'})
# print(list1)
location_names = []
for i in range(len(list1)):
    location_names.append(list1[i].find('a').text)

df = pd.DataFrame({'Location Names': location_names})
df.to_csv('Country Names.csv', index=False)

url2 = 'https://en.wikipedia.org/wiki/Lists_of_cities_by_country'
r2 = requests.get(url2)

city = []
soup = BeautifulSoup(r2.text, 'html.parser')
list1 = soup.findAll('b')
list1 = list1[1:]
list1 = list1[:-1]
list1 = [x.text.replace(' ', '_') for x in list1]
list1 = [x for x in list1 if 'List_of' in x]

new_r = requests.get('https://ontheworldmap.com/all/cities/')
soup2 = BeautifulSoup(new_r.text, 'html.parser')
new_list = soup2.findAll('div', attrs={'class': 'col-3'})[:3]
# city_names = new_list.find('li')
new_list = [x.findAll('li') for x in new_list]
for i in range(len(new_list)):
    for j in range(len(new_list[i])):
        city.append(new_list[i][j].find('a').text)

df2 = pd.DataFrame({'All city names': city})
df2.to_csv('List of all city names.csv', index=False)