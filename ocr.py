import collections
import requests
import re

site = requests.get('http://www.pythonchallenge.com/pc/def/ocr.html')
data = re.findall('(<!--.*-->)', site.text, re.DOTALL)

letters = collections.Counter(data[0])

rares = letters.most_common()[:-24-1:-1]

print(rares)

