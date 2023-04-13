
import os
import re

# define the directory path
directory = '/Users/yinxiaolong/Projects/Github/python/doc/'

# loop through all files and directories in the directory recursively



# regex that matches the string like 'ssis-345.mp4','ssq-234.mp4','hunbg 234.mp4','asd 234c.mp4'
regex = r'^\w{2,4}[- ]\d+\.mp4$'
def remove_file_name_suffix(file):
            if file.endswith('.mp4'):
                file_path = os.path.join(root, file)
                new_file_name = re.sub(r'(\d+).*', r'\1', file)
                print(new_file_name)
                

# loop through all files and directories in the directory recursively
for root, dirs, files in os.walk(directory):
    for file in files:
        # check if the file name starts with "test"
        if re.match(regex, file):
            # create the new file name by replacing "test" with "haola"
            new_file_name = file.replace('.mp4', 'haola')
            # create the full path of the old file
            old_file_path = os.path.join(root, file)
            # create the full path of the new file
            new_file_path = os.path.join(root, new_file_name)
            # rename the file
            os.rename(old_file_path, new_file_path)
            # check if the new file name contains non-ascii symbol
            if not re.match(regex, new_file_name.encode('ascii', 'ignore').decode('ascii')):
                print(f"{new_file_name} contains non-ascii symbol")

import requests
from bs4 import BeautifulSoup

# function to get the AV star's name based on the video id
def get_av_star_name(video_id):
    # construct the url
    url = f"https://www.javlibrary.com/en/vl_searchbyid.php?keyword={video_id}"
    # send a GET request to the url
    response = requests.get(url)
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")
    # find the div element that contains the AV star's name
    av_star_div = soup.find("div", {"class": "star-name"})
    # extract the AV star's name from the div element
    av_star_name = av_star_div.text.strip()
    return av_star_name

# example usage
print(get_av_star_name("ipx-999"))

import numpy as np
import gradio as gr

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]


def generate_tone(note, octave, duration):
    sr = 48000
    a4_freq, tones_from_a4 = 440, 12 * (octave - 4) + (note - 9)
    frequency = a4_freq * 2 ** (tones_from_a4 / 12)
    duration = int(duration)
    audio = np.linspace(0, duration, duration * sr)
    audio = (20000 * np.sin(audio * (2 * np.pi * frequency))).astype(np.int16)
    return (sr, audio)


gr.Interface(
    generate_tone,
    [
        gr.Dropdown(notes, type="index"),
        gr.Slider(minimum=4, maximum=6, step=1),
        gr.Textbox(type="number", value=1, label="Duration in seconds"),
    ],
    "audio",
).launch()

import os
import re

# define the directory path
directory = '/Users/yinxiaolong/Projects/jtlin/test/'

# loop through all files and directories in the directory recursively


for root, dirs, files in os.walk(directory):
    for file in files:
        # check if the file name starts with "test"
        if file.startswith
