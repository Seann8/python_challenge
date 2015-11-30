'''
Based on the clue given it is either a zipfile or pythons zip function
When looking at the  channel.zip we ca return a file for download
The easy way to process this would be to download the file into our
directory by hand and process the data however this solution uses
requests to pull the file automatically
'''

from zipfile import ZipFile
from getchallenge import challenge
from io import BytesIO

data = challenge("channel.zip")
zipped = BytesIO(data.content)
zipped = ZipFile(zipped)
stuff = {name: zipped.read(name) for name in zipped.namelist()}
## Seems to be a linked list again So i should call in the function I used before 
