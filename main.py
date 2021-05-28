"""
Inspired by:
https://towardsdatascience.com/how-to-build-an-mp3-music-player-with-python-619e0c0dcee2
"""

from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter.ttk import Progressbar
import pygame
import os
import sys

global num_pause, num_text, volume
num_pause = 0
volume = 1

music_player = Tk()
music_player.title("My Python Audio Player")
content = Frame(music_player)

directory = askdirectory()
os.chdir(directory)
dir_list = os.listdir()
songs_list = []
music_ext =('.mp3','.wav','m4a','flac','wma','aac')
for file in dir_list:
    if file.endswith(music_ext):
        songs_list.append(file)
    else:
        pass

num_songs = len(songs_list)

num_text = StringVar()
num_text.set("Click a song and play to begin!")

pause_str = StringVar()
pause_str.set("Pause")

var = StringVar()
play_list = Listbox(music_player, font="Calibri 12 bold",
fg="white", bg="blue", selectmode=SINGLE, width=100)


for song in songs_list:
    pos = 0
    play_list.insert(pos, song)
    pos = pos + 1

pygame.init()
pygame.mixer.init()

def play_song():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    var.set(play_list.get(ACTIVE))
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play()
    num_pause = 1
    num_text.set("Playing")

def stop():
    pygame.mixer.music.stop()
    sys.exit()

def pause_unpause():
    global num_pause, num_text, pause_str
    if num_pause == 0:
        pygame.mixer.music.pause()
        num_text.set("Paused")
        pause_str.set("Resume")
        song_length.stop()
        num_pause = 1
    else:
        pygame.mixer.music.unpause()
        num_text.set("Playing")
        pause_str.set("Pause")
        song_length.start(20)
        num_pause = 0

def next_song():
    pygame.mixer.music.load(play_list.get(ACTIVE))
    var.set(play_list.get(ACTIVE))
    var.set(play_list.get(next(play_list)))
    pygame.mixer.music.play()

def set_volume(pos):
    global volume
    volume = float(pos)/10
    pygame.mixer.music.set_volume(volume)

vol_var = DoubleVar()

play_button = Button(music_player, width=10, height=1, font="Calibri 14 bold",
text="Play", command=play_song, bg="white", fg="red")
pause_button = Button(music_player, width=10, height=1, font="Calibri 14 bold",
textvariable=pause_str, command=pause_unpause, bg="white", fg="red")
songs_text = Label(music_player, text="Songs Found: {}".format(num_songs))
song_status = Label(music_player, textvariable=num_text, font="Calibri 12 bold", bg="black",
fg='white')
next_button = Button(music_player, width=7, height=2, text="Next", command=next_song)
quit_button = Button(music_player, width=7, height=2, text="Quit", command=stop)
volume_slider = Scale(music_player, variable=vol_var, from_=0, to=10, orient=HORIZONTAL,
command=set_volume)
volume_label = Label(music_player, text="Volume Control")
song_length = Progressbar(music_player, orient=HORIZONTAL, length=750, mode='indeterminate')
song_length.start(20)

play_button.grid(column=0, row=0)
pause_button.grid(column=1, row=0)
quit_button.grid(column=2, row=0)
song_status.grid(column=1, row=2, columnspan=2)
volume_slider.grid(column=3, row=1)
volume_label.grid(column=3, row=0)
songs_text.grid(column=0, row=2)
play_list.grid(column=0, row=3, columnspan=4, rowspan=3)
song_length.grid(column=0, row=8, columnspan=4)
music_player.mainloop()
