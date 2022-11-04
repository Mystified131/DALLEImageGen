import openai
import webbrowser

#The image generations endpoint allows you to create an original image given a text prompt. Generated images can have a size of
#256x256, 512x512, or 1024x1024 pixels. Smaller sizes are faster to generate. You can request 1-10 images at a time using the n parameter.

openai.api_key = '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'

response = openai.Image.create(
    prompt = 'primitive Thomas cave abstract painting',
    n = 1,
    size = '1024x1024')

image_url = response['data'][0]['url']

#print(image_url)

webbrowser.open(image_url)