class VideoFile():
    def __init__(self,filename):
        if not filename.endswith(self.ext):
            raise Exception("Formato inválido")

class MP4File(VideoFile):
    ext="mp4"
    def play(self):
        print("Reproduzindo arquivo MP4!")

class WMVFile(VideoFile):
    ext="wmv"
    def play(self):
        print("Reproduzindo arquivo WMV!")

a1=MP4File("arquivo1.mp4")
a1.play()

a2=WMVFile("arquivo1.wmv")
a2.play()