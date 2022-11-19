from PIL import Image
from moviepy.editor import AudioFileClip, ImageClip
from moviepy.editor import *
import os
from functools import cache



OUTPUT = "out/finalVideo.mp4"
FINAL_IMAGE = "assets/images/final_image/myImagein4k.jpg"
FINAL_AUDIO = "assets/finalAudio/finalAudio.wav"

quality4kW = 1920
quality4kH = 1080











def change_img_quality(imagePath):
    image = Image.open(imagePath)
    new_image = image #.resize((quality4kW, quality4kH))
    new_image.save("assets/images/final_image/myImagein4k.jpg")




def add_static_image_to_audio(image_path, audio_path):

    # create the audio clip object
    audio_clip = AudioFileClip(audio_path)
    # create the image clip object
    image_clip = ImageClip(image_path)
    # use set_audio method from image clip to combine the audio with the image
    video_clip = image_clip.set_audio(audio_clip)
    # specify the duration of the new clip to be the duration of the audio clip
    video_clip.duration = audio_clip.duration
    # set the FPS to 1
    video_clip.fps = 1
    # write the resuling video clip
    video_clip.write_videofile("assets/videow/temp.mp4")


# change_img_quality("assets/images/raw_image/pexels-gigxels-com-7552122small1983.jpg")
def addIntroOutro(video_clip):
    intro = VideoFileClip("assets/Intro/Intro.mp4")
    outro = VideoFileClip("assets/Intro/Outro.mp4")
    video_clip = VideoFileClip("assets/videow/temp.mp4")
    final = concatenate_videoclips([intro, video_clip, outro])
    final.write_videofile(OUTPUT)

def makeVid(imagePath):
    change_img_quality(imagePath)
    add_static_image_to_audio(FINAL_IMAGE, FINAL_AUDIO)
    addIntroOutro("out/finalVideo.mp4")
    print("VIDEO MADE")



def getFileNameFromDirectory(directory):
    ls = os.listdir(directory)
    if ls.__contains__(".DS_Store"):
        list.remove(".DS_Store")
    return directory+ls[0]
