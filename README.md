## Gym Cardio Machine classification
### Model: Transfer Learning - MobileNetV2, Final Validation Accuarcy: 95.24%

## Usage
Run api_gym to start Flask
```
python api_gym.py
```

## use heroku API via url submit

```
import requests
# example url
pic_url = 'https://johnson.co.th/wp-content/uploads/2020/02/Horizon-Treadmill-T101-001.jpg'
url = f'https://gymcardio.herokuapp.com/url?p_image_url={pic_url}'
response = requests.get(url)
print(response.text)
```

## use heroku API via upload

```
import requests
# example image file
PATH_TO_INPUT_IMAGE = '/content/performance-treadmill-t900c.jpg'
img_file = {"file": open(PATH_TO_INPUT_IMAGE, "rb")}
url = "https://gymcardio.herokuapp.com/upload"
response = requests.post(url, files=img_file)
print(response.text)
```
## model training 
https://colab.research.google.com/drive/1Jw-2XhaAmHC2emX6qmxmWEU5VtyKbl9g?usp=sharing
