import glob
import sys
import os
import contextlib
import wave
import datetime
def get_length(fname):
    with contextlib.closing(wave.open(fname,'r')) as f:
        frames = f.getnframes()
        rate = f.getframerate()
        duration = frames / float(rate)
        return int(duration)

def get_paths_form_directory(directory):
    ls = os.listdir(directory)
    if ls.__contains__(".DS_Store"):
        list.remove(".DS_Store")
    return ls

def convert(n):
    return str(datetime.timedelta(seconds = n))


def format_file_name_for_timestamps(filepath, length, previousLength):
    
    filepath = str(filepath).removeprefix("assets/audio/ES_").removeprefix(".wav")
    
    return "  "+filepath+" , " + convert(previousLength) +" - "+ convert(length)+ "\n"





def concatenate_audio_wave(audio_clip_paths, output_path, textstamp_file):
    data = []
    # log file opening
    f = open(textstamp_file, 'w')
    previousTime = 0

    for clip in audio_clip_paths:
        w = wave.open(clip, "rb")
        lengthOfAudio = get_length(clip)
        data.append([w.getparams(), w.readframes(w.getnframes())])
        f.write(format_file_name_for_timestamps(clip, lengthOfAudio, previousTime))
        previousTime = lengthOfAudio
        w.close()

    f.close()
    output = wave.open(output_path, "wb")
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()



def prepend(list, str):  
    # Using format()
    str += '{0}'
    list = [str.format(i) for i in list]
    return(list)



# Take all the wav files in concatinate them and write on finalAudio nad log lenght on timestamps.txt
def conctatAudio_putFinalAudio(directoryName):
    files_path = prepend(get_paths_form_directory(directoryName), directoryName)
    print(files_path)
    print("CONCATINATING THE AUDIOS")
    concatenate_audio_wave(files_path, "assets/finalAudio/finalAudio.wav","assets/finalAudio/timestamps.txt" )

