from clarifai import rest
from clarifai.rest import ClarifaiApp
app = ClarifaiApp()
import os
from flask import Flask
from clarifai.rest import ClarifaiApp
import base64
# get the general model
# export CLARIFAI_API_KEY=f0bc502594a44e3986dd48ee7530aa22
app = Flask(__name__)
os.popen("export CLARIFAI_API_KEY=f0bc502594a44e3986dd48ee7530aa22")
@app.route("/caption/<string>")
def image_caption(string):
    image = base64.b64decode(string)
    app = ClarifaiApp(api_key='{api-key}')
    model = app.models.get("general-v1.3")
    #image = ClImage(file_obj=open(decoded_image, 'rb'))
    model.predict([image])
    print(os.popen("pwd").read())
    os.system("ls")
    return "lmao"

@app.route("/")
def main():
    return "hello"

if __name__ == "__main__":
    app.run(debug=True)

