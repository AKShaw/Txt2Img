from math import sqrt, ceil

class Txtp:
    def __init__(self, text, imgAR):
        self.text = text
        self.imgAR = imgAR

    def getRes(self, text, imgAR):
        txtHeight = ceil(sqrt(len(text)/imgAR))
        txtWidth = ceil(imgAR*txtHeight)
        res = [txtWidth, txtHeight]
        return res

    def getTextRes(self):
        return self.getRes(self.text, self.imgAR)