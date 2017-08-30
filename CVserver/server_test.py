from clarifai import rest
from clarifai.rest import ClarifaiApp
import base64
from flask import Flask, jsonify, request
app2 = ClarifaiApp()

from clarifai.rest import ClarifaiApp


app = Flask(__name__)


# get the general model
#model = app2.models.get("general-v1.3")

# predict with the model
#with open("test_image.jpg", "rb") as image_file:
#    encoded_string = base64.b64encode(image_file.read())
#print(encoded_string)
#print(model.predict_by_filename(filename="test_image.jpg"))

@app.route("/")
def main():
	return "Hello bro"



@app.route("/v1/caption/", methods = ["POST","GET"])
def caption():
	image_encoded = request.get_data(parse_form_data=True)
	print(type(image_encoded))
	#print(image_encoded["image_data"])
	model = app2.models.get("general-v1.3")
	return jsonify(model.predict_by_base64(base64_bytes=image_encoded))
        

if __name__ == "__main__":
	app.run()
