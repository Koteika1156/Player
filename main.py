from tkinter import filedialog
from tkinter import Tk
from tkinter import Menu
from tkinter import END
from tkinter import Listbox
from tkinter import PhotoImage
from tkinter import Button
from tkinter import Frame
import pygame
import os

root = Tk()
root.title('DenisPlayer')
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)

songs = []


class Constants:
    current_song = ""
    paused = False


def load_music():
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == '.mp3':
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    Constants.current_song = songs[songlist.curselection()[0]]


def play_music():

    if not Constants.paused:
        pygame.mixer.music.load(os.path.join(root.directory, Constants.current_song))
        pygame.mixer.music.play()

    else:
        pygame.mixer.music.unpause()
        Constants.paused = False


def pause_music():
    pygame.mixer.music.pause()
    Constants.paused = True


def next_music():

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(Constants.current_song) + 1)
        Constants.current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


def back_music():
    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(Constants.current_song) - 1)
        Constants.current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass


organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label='Select Folder', command=load_music)
menubar.add_cascade(label='Organise', menu=organise_menu)

songlist = Listbox(root, bg="red", fg="white", width=100, height=15)
songlist.pack()

play_btn_image = PhotoImage(file='play.png')
pause_btn_image = PhotoImage(file='pause.png')
next_btn_image = PhotoImage(file='next.png')
back_btn_image = PhotoImage(file='back.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame, image=play_btn_image, borderwidth=0, command=play_music)
pause_btn = Button(control_frame, image=pause_btn_image, borderwidth=0, command=pause_music)
next_btn = Button(control_frame, image=next_btn_image, borderwidth=0, command=next_music)
back_btn = Button(control_frame, image=back_btn_image, borderwidth=0, command=back_music)

play_btn.grid(row=0, column=1, padx=7, pady=10)
pause_btn.grid(row=0, column=2, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
back_btn.grid(row=0, column=0, padx=7, pady=10)

root.mainloop()
