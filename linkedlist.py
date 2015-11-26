import requests
import re


uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php"

nothing_rep = "and the next nothing is "

nothing = "12345"
for i in range(400):
    
    try:
        r = requests.get(uri+"?nothing="+nothing)
        foo = re.search('[-+]?\d+[\.]?\d*', r.text)
        nothing = foo.group(0)
        print(r.text)
    except AttributeError as e:
        print(r.text)
        nothing = input("give me a new number")

        
