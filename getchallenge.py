# challenge getter for python challenge
import requests


def challenge(clue):
    urlstart = "http://www.pythonchallenge.com/pc/def/"
    r = requests.get(urlstart + clue)
    return r

if __name__ == "__main__":
    crumb = input("please enter your clue")
    challenge = getchallenge(crumb)
    print(challenge)
