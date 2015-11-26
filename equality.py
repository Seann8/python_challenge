import requests
import re


r = requests.get("http://www.pythonchallenge.com/pc/def/equality.html")

data = re.findall('[^A-Z]+[A-Z]{3}[a-z]{1}[A-Z]{3}[^A-Z]+', r.text, re.DOTALL)
# finds a list of matches

urlstart = "http://www.pythonchallenge.com/pc/def/"

for i in data :
    print(i)

    
def webcheck(link):  # Check to see if Url is good
    r = requests.head(link)
    return r.status_code == requests.codes.ok


for i in data:  # Loop through answers
    answer = webcheck((urlstart + i + ".html"))
    if answer is True:
        print(answer)
        print(i)
