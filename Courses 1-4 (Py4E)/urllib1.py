from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

sum=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url='http://py4e-data.dr-chuck.net/comments_663888.html'
html=urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    lst=re.findall('([0-9]+)',str(tag))
    for nos in lst:
        sum+=int(nos)

print(sum)
