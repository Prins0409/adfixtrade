import requests
from bs4 import BeautifulSoup

url = "https://www.uniononline.co.uk/middle-east/en/sitemap.xml"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')

for links in soup.find_all('loc'):
    print(links.text)