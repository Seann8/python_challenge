from zipfile import ZipFile
from getchallenge import challenge
from io import BytesIO

data = challenge("channel.zip")
zipped = BytesIO(data.content)
zipped = ZipFile(zipped)
