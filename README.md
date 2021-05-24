## Gym Cardio Machine classification
### Model: MobileNetV2

## Usage
Run api_gym to start Flask
```
python api_gym.py
```

# #---------------------------------#
# # To use this api in Python
# #---------------------------------#
# import requests
# # upload your image to colab
# PATH_TO_INPUT_IMAGE = '/content/1062404-1573963307-167380.jpg'
# img_file = {"file": open(PATH_TO_INPUT_IMAGE, "rb")}
# '''
# The instance "file" is created in the api_gym.py 
# See the line includig: 
# file = request.files['file']
# '''
# url = "https://gymcardio.herokuapp.com/upload"
# response = requests.post(url, files=img_file)
# print(response.text)