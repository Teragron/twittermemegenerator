import os
import cv2
import time
import tweepy
import random
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


all_keys = open("twitterkeys.txt", "r").read().splitlines()
api_key = all_keys[0]
api_key_secret = all_keys[1]
access_token = all_keys[2]
access_token_secret = all_keys[3]

authenticator = tweepy.OAuthHandler(api_key, api_key_secret)
authenticator.set_access_token(access_token, access_token_secret)

api = tweepy.API(authenticator, wait_on_rate_limit=True)

def tweet(metin, foto):
    media = api.media_upload(filename=foto, )
    print("MEDIA: ", media)

    tweet = api.update_status(status=metin, media_ids=
    [media.media_id_string])
    print("TWEET: ", tweet)



vegetables = ["Broccoli", "Musroom", "Eggplant", "Onion", "Spaghetti", "Cauliflower", "Oatmeal"]
kutup = [["a", "b"]]

imgExtension = ["png", "jpeg", "jpg"]
allImages = list()

def fotosec(directory="wth/"):
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice] #Do Whatever you want with the image file
    return chosenImage

def tweetat():
    randomImage = fotosec()
    tam(randomImage)
    dir = 'temp'
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))
    img = Image.open('wth/on.png')

    width, height = img.size

    #font_type = ImageFont.truetype("arial.ttf", 18)

    font_type = ImageFont.truetype("tnr.ttf", int(width/13)) #12.8
    secim = random.choice(vegetables)
    I1 = ImageDraw.Draw(img)
    yazikirli = f"What the fuck is {secim}?"
    yazitemiz = f"What the f*** is {secim}?"
    yol = f"alinti/{randomImage}"
    # Add Text to an image
    I1.text((60, 50), yazikirli, font=font_type, fill=(255, 255, 255))
    img.save(yol)
    if kutup[-1] not in [yazikirli, randomImage]:
        kutup.append([yazikirli, randomImage])
        tweet(yazitemiz, yol)


import os
import cv2
import time
import tweepy
import random
import requests
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageOps


def dondur_parent(yol):
    img = Image.open(yol)
    #img.putalpha(60)  # Half alpha; alpha argument must be an int
    mirror_img = ImageOps.mirror(img)
    mirror_img.save("temp/donmus.png")

def zoomat(foto, zoom):
    img = Image.open(foto)
    w, h = img.size
    x = int(w/2)
    y = int(h/2)
    zoom2 = zoom * 2
    img = img.crop((x - w / zoom2, y - h / zoom2,
                    x + w / zoom2, y + h / zoom2))
    img.resize((int(w/2), int(h/2)), Image.LANCZOS)
    img.save("temp/zoom.png")


def yapistir(arka, on):
    background = Image.open(arka)
    foreground = Image.open(on)
    w, h = background.size
    background.paste(foreground, (int(w/1.7), int(h/100)), foreground)
    background.save("wth/on.png")


def tam(yol):
    zoomat(f"wth/{yol}", 1.5)
    dondur_parent("temp/zoom.png")
    im = Image.open("temp/donmus.png")
    angle = 90
    out = im.rotate(angle, expand=True)
    out.save("temp/donmus2.png")
    img = cv2.imread("temp/donmus2.png")
    ht, wd = img.shape[:2]
    pct = 80
    ht2 = int(ht*pct/100)
    ht3 = ht - ht2
    top = np.full((ht3,wd), 255, dtype=np.uint8)
    btm = np.linspace(255, 0, ht2, endpoint=True, dtype=np.uint8)
    btm = np.tile(btm, (wd,1))
    btm = np.transpose(btm)
    alpha = np.vstack((top,btm))
    result = img.copy()
    result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
    result[:,:,3] = alpha
    cv2.imwrite("temp/donmus3.png", result)
    im = Image.open("temp/donmus3.png")
    angle = -90
    out = im.rotate(angle, expand=True)
    out.save("temp/on.png")
    yapistir(f"wth/{yol}", "temp/on.png")

def fotosec(directory="wth/"):
    for img in os.listdir(directory): #Lists all files
        ext = img.split(".")[len(img.split(".")) - 1]
        if (ext in imgExtension):
            allImages.append(img)
    choice = random.randint(0, len(allImages) - 1)
    chosenImage = allImages[choice] #Do Whatever you want with the image file
    return chosenImage

vegetables = ["Broccoli", "Musroom", "Eggplant", "Onion", "Spaghetti", "Cauliflower", "Oatmeal"]
kutup = [["a", "b"]]

imgExtension = ["png", "jpeg", "jpg"]
allImages = list()



if __name__ == "__main__":
    while True:
        num = random.randint(1, 10)
        tweetat()
        time.sleep(2700+num)
