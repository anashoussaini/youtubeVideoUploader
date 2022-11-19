from audio_func import *
from image_func import *
import time
import shutil
# def getImage
# def fuseAudio&Image
# def makeAnimation
# def makeVideo

# Take all the wav files in concatinate them and write on finalAudio nad log lenght on timestamps.txt

#conctatAudio_putFinalAudio("assets/audio/")
#makeVid("assets/images/raw_image/myImagein4k 10.37.04 PM.jpg")
def emptyDirectory(folder):
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))


def clearDirectories():
    emptyDirectory("assets/audio")
    emptyDirectory("assets/images/final_image")
    emptyDirectory("assets/images/raw_image")




if __name__ == '__main__':
    start = time.time()
    conctatAudio_putFinalAudio("assets/audio/")
    makeVid("assets/images/raw_image/image.jpg")
    print(getFileNameFromDirectory("assets/images/raw_image/"))
    end = time.time()
    print(end - start)
    clearDirectories()