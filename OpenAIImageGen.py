import openai
import webbrowser
from six.moves import urllib
import os
import datetime
import time

#The image generations endpoint allows you to create an original image given a text prompt. Generated images can have a size of
#256x256, 512x512, or 1024x1024 pixels. Smaller sizes are faster to generate. You can request 1-10 images at a time using the n parameter.

varnum = 10

openai.api_key = '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'

for cops in range(varnum):

    print("")

    print('Generating Image: ', str(cops + 1))

    print("")

    right_now = datetime.datetime.now().isoformat()
    list = []

    for i in right_now:
        if i.isnumeric():
            list.append(i)

    tim = ("".join(list))

    openai.api_key = openaikey

    response = openai.Image.create(
        prompt = 'primitive Thomas cave abstract painting',
        n = 1,
        size = '1024x1024')

    image_url = response['data'][0]['url']

    #print(image_url)

    prom = 'primitive Thomas cave abstract painting'

    titstr = prom.replace(' ', '')

    ur3 = 'C:\\Users\\mysti\\Downloads\\' + titstr + '_' + tim + '.png'

    urllib.request.urlretrieve(image_url, ur3)

    #webbrowser.open(image_url)

    time.sleep(15)

print("")

print("Image generation complete. Check your Downloads folder for saved image files.")

print("")