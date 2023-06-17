import cx_Freeze
import sys
base = None

if sys.platform == "win32":
    base = "Win32GUI"

exeList = [cx_Freeze.Executable("TextToSpeechApp.py",base=base)]

cx_Freeze.setup(name = "Text-To-Speech-App-v1.0",
                options = {"build_exe":{"packages":["tkinter","gtts"]}},
                version = "1.0",
                description = "Text to Speech Application created by ngvkien, Copyright: 2023",
                executables = exeList)
