# s24028
# 沖縄県の人口を取得するプログラム

import requests
from bs4 import BeautifulSoup

url = 'https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html'
response = requests.get(url)
response.encoding = 'shift_jis'

soup = BeautifulSoup(response.text, 'html.parser')

population_data = soup.find_all('td', align='right')

total_population = population_data[0].get_text(strip=True)
male_population = population_data[1].get_text(strip=True)
female_population = population_data[2].get_text(strip=True)

print(f"総人口: {total_population}")
print(f"男: {male_population}")
print(f"女: {female_population}")