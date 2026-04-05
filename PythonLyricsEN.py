
import tkinter as tk

from tkinter import messagebox


def savetitle():
    global title
    title = titlebox.get()
    openlyricswindow()


def openlyricswindow():
    global lyricswindow, lyricsbox, lyricsbutton

    lyricswindow = tk.Toplevel(root)
    lyricswindow.title("Lyrics")

    lyricsindications = tk.Message(lyricswindow, text="Paste the lyrics line by line")
    lyricsindications.pack()

    lyricsbutton = tk.Button(lyricswindow, text="Sing", command=savelyrics)
    lyricsbutton.pack()

    exitlyricsbutton = tk.Button(lyricswindow, text="Exit", command=leave)
    exitlyricsbutton.pack()

    lyricsbox = tk.Text(lyricswindow)
    lyricsbox.pack()


def sing(title):
    with open("lyrics.txt", "r") as l:
        lyrics = l.readlines()
    for line in lyrics:
        if line.strip() != "":
            messagebox.showinfo(title, line)
        else:
            messagebox.showinfo(title, "*Music*")


def savelyrics():
    lyrics = lyricsbox.get(1.0, "end")
    with open("lyrics.txt", "w") as l:
        l.write(lyrics)
    lyricsbutton.config(state="disabled")
    sing(title)
    lyricswindow.destroy()


def leave():
    root.destroy()



root = tk.Tk()

root.title("Song title")

songtitlewindow = root

songtitleindication = tk.Message(songtitlewindow, text="Enter song title")
songtitleindication.pack()

titlebutton = tk.Button(songtitlewindow, text="Next", command=savetitle)
titlebutton.pack()

exitbutton = tk.Button(songtitlewindow, text="Exit", command=leave)
exitbutton.pack()

titlebox = tk.Entry(songtitlewindow)
titlebox.pack()

root.mainloop()





