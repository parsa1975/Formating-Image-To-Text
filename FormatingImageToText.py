from guizero import *
from pywhatkit import image_to_ascii_art as formating
app = App("Formating")
imageName = TextBox(app,"Image Address")
fileName = TextBox(app,"File Address")
def formatingFunc():
    app.info("Formating","Runing Formating Level")
    formating(imageName.value,fileName.value)
    app.info("Formating","Done!")
PushButton(app,text = "Formating",command = formatingFunc)
app.display()