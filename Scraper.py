import requests
from bs4 import BeautifulSoup

url = "https://dining.unc.edu/locations/chase/"
data = requests.get(url)
html = data.text

print(html)