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
import re


data = challenge("channel.zip")
zipped = BytesIO(data.content)   # takes the data in as bytestream data
# lets us work entirely in memory

zipped = ZipFile(zipped)
# | converts the zipfile into a dictionary using
# V the names as keys and the contents as values
stuff = {name: zipped.read(name).decode("utf-8") for name in zipped.namelist()}
stuff = stuff


def linkedPy(start, files):  # function to go through the dictionary
    text = str(files.get(start))
    pat = re.search('[-+]?\d+[\.]?\d*', text)
    if pat is None:
        return "not a file"
    else:
        return pat.group(0)  # returns a string result from re.search

out = []
clue = '90052.txt'  # from the readme file in the archive
for i in range(len(zipped.namelist())):
    step = linkedPy(clue, stuff)
    if step == 'not a file':
        break
    else:
        out.append(step)
    clue = step + '.txt'
print(''.join([zipped.getinfo('{}.txt'.format(i)).comment.decode('utf-8') for i in out]))
