import os.path
import io
from PIL import Image

import requests

class Character:
    def __init__(self,name, gender , species, origin, status , images, numberOfEps):
        self.name = name
        self.gender = gender
        self.species = species
        self.origin = origin
        self.status = status
        self.image_url = images
        self.numberOfEps = numberOfEps
        self.imageName= self.name.replace(" ","")+".png"
        self.imagePath = "./images/"+self.imageName
        self.downloadImage()

    def show_character(self):
        print(self.name , self.gender)


    def downloadImage(self):
        #check if file does not exist then download image
        if not os.path.exists(self.imagePath):
            response = requests.get(self.image_url)
            imgData = response.content
            image = Image.open(io.BytesIO(imgData))

            #resize 
            image = image.resize((200,200),Image.ANTIALIAS)
            image.save(self.imagePath)

            print(self.name + "Is downloaded")

    def getImage(self):
        return Image.open(self.imagePath)

