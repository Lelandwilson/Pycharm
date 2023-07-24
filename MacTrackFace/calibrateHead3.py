import time
from mutagen.mp3 import MP3
from pygame import mixer
import os.path
from gtts import gTTS
import AppKit


class DetectMonitors():

    def detect_monitors(self):
        screens = AppKit.NSScreen.screens()

        monitor_count = len(screens)
        # print("Number of connected monitors:", monitor_count)

        monitors = []
        for i, screen in enumerate(screens):
            description = screen.deviceDescription()
            display_id = description["NSScreenNumber"]
            name = screen.localizedName()
            frame = screen.frame()
            width = frame.size.width
            height = frame.size.height

            monitor_info = {
                "Monitor": i+1,
                "Name": name,
                "Display ID": display_id,
                "Width": width,
                "Height": height
            }
            monitors.append(monitor_info)

        return monitors


def run(point, i, monitors):
    arrarOfPoints = []
    # Detect number of monitors & monitor details: returns a dictionary of monitors
    monitors = DetectMonitors().detect_monitors()
    calibrate().speakCommand(i, monitors)  # Command to look at each screen
    arrarOfPoints.append(point)  # Add measured angles to temp array

    return arrarOfPoints  # export array of angles


class calibrate:
    def __init__(self):
        mixer.init()

    def get_duration(self, file_path):
        audio = MP3(file_path)
        return audio.info.length

    def speak(self, file):
        mixer.music.load(file)  # Loads the mp3 file
        mixer.music.play()
        duration = self.get_duration(file)  # Use self to access the method within the class
        time.sleep(duration)

    def speakCommand(self, currentScreenNo, monitorsDictionary):
        # If voice file does not exist, create it
        if not os.path.isfile(f'./screen{currentScreenNo}.mp3'):
            tts = gTTS(text=f'Look at screen {currentScreenNo}', lang='en')
            tts.save(f'./screen{currentScreenNo}.mp3')

        # Speak the command
        self.speak(f'screen{currentScreenNo}.mp3')

        if currentScreenNo != len(monitorsDictionary):
            time.sleep(0.3)
            self.speak('next.mp3')




