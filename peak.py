#  practice with pickle
import requests
import pickle

r = requests.get("http://www.pythonchallenge.com/pc/def/banner.p")
data = r.text
jar = pickle.loads(bytes(data, "UTF-8"))


for lines in jar :
    print("".join(i[0]*(i[1]) for i in lines))

