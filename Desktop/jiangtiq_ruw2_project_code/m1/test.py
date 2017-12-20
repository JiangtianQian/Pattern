from bs4 import BeautifulSoup
import requests


response = requests.get('https://www.change.org/t/human-rights-11?source_location=topic_page')


soup = BeautifulSoup(response.text)
#print soup
links = soup.find_all("a", attrs={"class":"title clearfix link-block"})
#print links
for link in links:
    print {'link': link}

