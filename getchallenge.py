# challenge getter for python challenge
import requests


class Challenge(object):
    """ a class to collect and process the challenges using requests """
    def __init__(self, clue):
        self.clue = clue

    def gethtml(self):
        urlstart = "http://www.pythonchallenge.com/pc/def/"
        r = requests.get(urlstart + self.clue)
        return r

if __name__ == "__main__":
    crumb = input("please enter your clue")
    test = Challenge(crumb)

    print(test.gethtml())
