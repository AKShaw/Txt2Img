from PIL import Image, ImageChops
import sys, os
from imp_file import *
from txtp_file import *

def getCLA(arg):
    try:
        return sys.argv[arg]
    except IndexError:
        if (arg == 1):
            print("Please specify an input image file!")
        elif (arg == 2):
            print("Please specify an input txt file!")
        elif (arg==3):
            print("Please enter 'crop' or 'nocrop'")
        exit()

def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0,0)))
    diff = ImageChops.difference(im, bg)
    diff = ImageChops.add(diff, diff, 2.0, -100)
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)

def loadImg(img):
    try:
        if (getCLA(3)=="crop"):
            return trim(Image.open(img))
        elif(getCLA(3)=="nocrop"):
            return Image.open(img)
    except FileNotFoundError:
        print(img + " not found!")

def loadTxt(txt):
    try:
        file = open(txt, "r")
        return file.read()
    except FileNotFoundError:
        print (txt + " not found!")

def checkHelp():
    if(getCLA(1)=="help" or getCLA(1)=="-help"):
        print("USAGE: 'python main.py <image file> <text file> <crop/nocrop>")
        exit()

def start():
    checkHelp()
    img = loadImg(getCLA(1))
    text = loadTxt(getCLA(2))
    imp = Imp(img)
    imgAR = imp.getAspectRatio()
    txtp = Txtp(text, imgAR)
    txtRes = txtp.getTextRes()
    imgRes = imp.getRes()
    imp.findChunkSize(txtRes, imgRes)



start()