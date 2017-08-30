from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

#General model
model = app.models.get('general-v1.3')

response = model.predict_by_url(url='https://samples.clarifai.com/metro-north.jpg')

print(response)
