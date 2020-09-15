from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

urls=list()

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/known_by_Ruairi.html'
html=urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('a')
for tag in tags:
    lst=re.findall('href=(".+")',str(tag))
    urls.extend(lst)

print(urls[17:18])
