import requests
import json
from bs4 import BeautifulSoup
url="https://api.exchangerate.host/latest?base=USD"
response=requests.get(url)
soup=BeautifulSoup(response.text,"html.parser")
convert=json.loads(response.text)["rates"]
def Convert(country):
    return convert[country.upper()]
# print(Convert("uzs"))
keys = convert.keys()
