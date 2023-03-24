from ssl import OP_NO_RENEGOTIATION
import requests
from tkinter import *
from PIL import Image,ImageTk
from Character import Character
from Scrollable import ScrollableFrame

def loadData():
    url = 'https://rickandmortyapi.com/api/character/?page=1'
    response=requests.get(url)

    jsonResponse = response.json()
    jsonRes_Results = jsonResponse['results']
    characters = []

    for obj in jsonRes_Results:
        name = obj['name']
        gender = obj['gender']
        species = obj['species']
        origin = obj['origin']['name']
        status = obj['status']
        image_url = obj['image']
        numberOfEps = len(obj['episode'])
        character = Character(name, gender, species, origin, status, image_url, numberOfEps)
        characters.append(character)

    return   characters
    
characters = loadData()

# Creating UI with Tkinter

root= Tk()

root.title("Rick and Morty Python API")
root.geometry("535x560")
root.update()
root.resizable(0,0)

scrollable = ScrollableFrame(root)

for char in characters :
    # main item frame for each character
    listItemFrame = Frame(scrollable.scrollable_frame, borderwidth=4, relief=GROOVE)
    listItemFrame.pack(fill= X ,padx=7.5)

    # left(image) frame
    leftFrame = Frame(listItemFrame)

    leftFrame.grid(row=0,column=0,padx = 7.5, pady=15)

    # load image
    photo=ImageTk.PhotoImage(char.getImage())
    imageLabel = Label(leftFrame, image= photo)
    imageLabel.image = photo
    imageLabel.pack(fill = BOTH, expand = True)


    # right(lable) frame
    rightFrame = Frame(listItemFrame)

        # labels
    Label(rightFrame, text ="Name: "+char.name, font=("Times New Roman", 12), padx=7.5).pack(anchor = 'w', expand= True)
    Label(rightFrame, text ="Species: "+char.species, font=("Times New Roman", 12), padx=7.5).pack(anchor = 'w', expand= True)
    Label(rightFrame, text ="Gender: "+char.gender, font=("Times New Roman", 12), padx=7.5).pack(anchor = 'w', expand= True)
    Label(rightFrame, text ="Origin: "+char.origin, font=("Times New Roman", 12), padx=7.5).pack(anchor = 'w', expand= True)
    Label(rightFrame, text ="Status: "+char.status, font=("Times New Roman", 12), padx=7.5).pack(anchor = 'w', expand= True)
    Label(rightFrame, text =str(char.numberOfEps) +" Episodes", font=("Times New Roman", 12), padx=7.5).pack(anchor = 'w', expand= True)

    rightFrame.grid(row=0,column=1,sticky = 'we')


scrollable.pack(fill = BOTH, expand= True)




root.mainloop()