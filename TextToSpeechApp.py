from gtts import gTTS
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

initDir = "C:\\"
mytld = "com.vn"
myLang = "vi"

ttsWin = Tk()
ttsWin.title("Google Text to Speech")
ttsWin.geometry('400x300')

fLabel = Label(ttsWin, text = "Text file")
fLabel.place(x = 20, y = 30)

fText = StringVar()
fEntry = Entry(ttsWin, textvariable = fText, width = 35)
fEntry.place(x = 70, y = 30)

def BrowserFile():
    fPath = filedialog.askopenfilename(initialdir = initDir, filetypes = [("Text file", "*.txt")])
    fEntry.insert(INSERT, fPath)
    #fPath = fText.get()
    #initDir = fPath

def ToSpeech():
    try:
        fPath = fText.get()
        with open(fPath, 'r', encoding = 'utf-8') as fid:
            text = fid.read()
        #print(fPath)
        #print(text)
        myApp = gTTS(text, tld = mytld, lang = myLang)
        sFile = filedialog.asksaveasfile(initialdir=initDir,
                                             defaultextension=".mp3",
                                             filetypes=[("MP3 file",".mp3"),
                                                       ("WMA file",".wma"),
                                                        ("WAV file", ".wav")])
        #print(sFile.name)
        myApp.save(sFile.name)
        messagebox.showinfo(title = "Convert to Speech", message = "Convert to Speech Successfully")
    except:
        messagebox.showerror(title = "Convert to Speech", message = "Convert to Speech Unsuccessfully")
                                     
fButton = Button(ttsWin, text = "Browser...", command = BrowserFile)
fButton.place(x = 300, y = 30)

fConv = Button(ttsWin, text = "Convert to Speech", command = ToSpeech)
fConv.place(x = 70, y = 80)

if __name__ == "__main__":
    ttsWin.mainloop()
