import boto3
from pprint import pprint
import image_helpers

client = boto3.client('rekognition')

img = '' #insert image

imgbytes = image_helpers.get_image_from_url(img)

rekresp = client.detect_labels(Image={'Bytes':imgbytes},MinConfidence=1)

print("Here's what I see in the image:")
for label in rekresp['Labels']:
    print(label['Name'])
