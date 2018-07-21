import io 
from google.cloud import vision 
from google.cloud.vision import types 
vision_client = vision.ImageAnnotatorClient() 
file_name = 'hjacksonbrownjr1-2x.jpg' 
with io.open(file_name,'rb') as image_file: 
        content = image_file.read() 
        image = types.Image(content=content) 
response = vision_client.text_detection(image=image) 
texts = response.text_annotations 
for text in texts: 
        print(text.description)