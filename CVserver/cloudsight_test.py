import cloudsight
from flask import Flask
import os
import sys

# INIT
#api_key = "q1RmugXxnjuAa_4mBSW93w"
#secret = "M8z18rMeiyenNIntIevW1Q"
api_key = "8ZyGYkpmEVK1wJDb5uiBog"
secret = "tx25bk7L_J-DqLPCkDBrOg"
#auth = cloudsight.SimpleAuth(api_key)
auth = cloudsight.OAuth(api_key, secret)
api = cloudsight.API(auth)

with open('test_image.jpg', 'rb') as f:
    response = api.image_request(f, 'your-file.jpg', {
        'image_request[locale]': 'en-US',
    })

status = api.wait(response['token'], timeout=30)


