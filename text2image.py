import requests, base64
import numpy as np
from PIL import Image

def text2image(term):
    url= base64.b64decode('aHR0cHM6Ly92aXNpb24tZXhwbG9yZXIuYWxsZW5haS5vcmcvYXBpL3hseG1lcnQ=')
    headers = {
        'accept': 'application/json, text/plain, */*',
        'Content-Type': 'multipart/form-data; boundary=---------------------------1',
    }
    data = '''-----------------------------1\nContent-Disposition: form-data; name="params"\n\n{"caption":"''' + term + '''","hasImage":false}\n-----------------------------1--'''
    response = requests.post(url=url, headers=headers, data=data)
    content = response.json()
    image_pxls = content["answer"]["image"]
    pxlarray = np.array(image_pxls, dtype=np.uint8)
    image = Image.fromarray(pxlarray)
    return image
