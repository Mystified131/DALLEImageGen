import openai
import webbrowser
from six.moves import urllib
import os
import datetime
import time
from TextGetter import GetWebText
from RandFunct import random_number
from RandFunct2 import random_number2
from subprocess import call

#The image generations endpoint allows you to create an original image given a text prompt. Generated images can have a size of
#256x256, 512x512, or 1024x1024 pixels. Smaller sizes are faster to generate. You can request 1-10 images at a time using the n parameter.

varnum = 5

imglst = GetWebText()

txlen = len(imglst)

prom = ""

prlen = random_number2(5,9)

for txad in range(prlen):
    txchos = random_number(txlen)
    txstr = imglst[txchos]
    #txstr = txstr.replace('.', '')
    prom += txstr
    prom += " "

prom = prom[:-1]

print("")

print('Prompt is: ', prom)

print("")

openai.api_key = openaikey

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
        prompt = prom,
        #prompt = 'primitive Thomas cave abstract painting',
        n = 1,
        size = '1024x1024')

    image_url = response['data'][0]['url']

    #print(image_url)

    titstr = prom.replace(' ', '')

    ur3 = 'C:\\Users\\mysti\\Downloads\\' + titstr + '_' + tim + '.png'

    urllib.request.urlretrieve(image_url, ur3)

    #webbrowser.open(image_url)

    time.sleep(15)

print("")

print("Image generation complete. Check your Downloads folder for saved image files.")

print("")

call(["python", "OpenAIRanImageGen.py"])