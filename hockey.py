from getchallenge import challenge
from PIL import Image
from io import BytesIO
clue = "hockey.html"

problem = challenge(clue)
print(problem.text)

'''
Its in the air . look at the letters  if we look at the letters
that make up hockey they spell oxygen  so lets try that one
'''

clue2 = 'oxygen.html'

problem = challenge(clue2)
print(problem.text)

'''
a png file , looks like image processing may be needed
so the image has a band of grey pixels this bad must be my encoded data
I need to figure out a way to read it
'''
clue3 = 'oxygen.png'
problem = challenge(clue3)

pic = Image.open(BytesIO(problem.content))
