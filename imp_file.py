from math import ceil

class Imp:
    def __init__(self, img):
        self.img = img
        self.width, self.height = img.size
        self.aspectRatio = self.width/self.height
        self.imgChunkSize = [0,0]

    def getRes(self):
        return [self.width, self.height]


    def getAspectRatio(self):
        return self.aspectRatio

    def findChunkSize(self, txtRes, imgRes):
        chunkSize = [0,0]
        for i in range(2):
            chunkSize[i] = ceil(imgRes[i]/txtRes[i])
        self.imgChunkSize=chunkSize

    def getImgChunkSize(self):
        return self.imgChunkSize

