import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://docs.google.com/document/d/e/2PACX-1vQGUck9HIFCyezsrBSnmENk5ieJuYwpt7YHYEzeNJkIb9OSDdx-ov2nRNReKQyey-cwJOoEKUhLmN9z/pub"
r = requests.get(url)
#print(r)
soup = BeautifulSoup(r.text, "lxml")

table = soup.find("table")
print(table)