import requests
from PIL import Image
from io import BytesIO

response = requests.get('https://cataas.com/cat/gif')
img = Image.open(BytesIO(response.content))

img.save('cat.gif')

