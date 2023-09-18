# Google forms link
# https://docs.google.com/forms/d/e/1FAIpQLSeL_c2Kl9N3mDaig6uNzmtEwfdSHKAjGF7_-ExmRia4TgtwCA/viewform?usp=sf_link
# https://myhttpheader.com/
import requests
from bs4 import BeautifulSoup
#
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language":"en-US,en;q=0.9,es-419;q=0.8,es;q=0.7",
    "sec-fetch-site":"cross-site",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "sec-ch-ua-mobile":"?0",
    "sec-ch-ua-platform":"Windows",
    "Accept-Encoding":"gzip, deflate br",
    "Accept-Language":"en-US,en;q=0.9,es-419;q=0.8,es;q=0.7",
    "Cookie": "PHPSESSID=c7fae6993366adf72ee49c16223755c1; _ga=GA1.2.1198691029.1693231842; _ga_VL41109FEB=GS1.2.1693251165.3.1.1693251772.0.0.0"
}

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
#     "Accept-Language":"en-US,en;q=0.9,es-419;q=0.8,es;q=0.7"
# }

url = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
response = requests.get(url, headers = headers)
response.status_code
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")


# Use BeautifulSoup/Requests to scrape all the listings from the Zillow web address (Step 4 above).
link = soup.find_all("a")

# Create a list of links for all the listings you scraped. e.g.
#
# Create a list of prices for all the listings you scraped. e.g.