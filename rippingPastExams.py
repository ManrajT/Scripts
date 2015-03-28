from mechanize import Browser
from bs4 import BeautifulSoup
import os.system

br = Browser()

br.open('http://engsoc.uwaterloo.ca/user')

br.select_form(nr=1)

br[“name”] = “mtatla”
br[“pass”] = “password”

file = br.open(“page”)

links = []

for link in soup.final_all(‘a’):
  if “pdf” in link:
	links.append(link)

for url in links
  os.system(“curl -O http://engsoc.uwaterloo.ca” + url)

