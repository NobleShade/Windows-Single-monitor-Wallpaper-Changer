#Import the libraries we need to interact with the Windows API, handle file paths, and select a random image from a folder.
import comtypes
import comtypes.client
import ctypes
import random
from pathlib import Path

#Recognize the monitor dimensions 
class RECT(ctypes.Structure):
    _fields_ = [("left", ctypes.c_long),
                ("top", ctypes.c_long),
                ("right", ctypes.c_long),
                ("bottom", ctypes.c_long)]
    
#Recognize the Windows interface and pass it to Python so that it can understand and give the precise order to change the desktop wallpaper.
class IDesktopWallpaper(comtypes.IUnknown):
    _iid_ = comtypes.GUID("{B92B56A9-8B55-4E14-9A89-0199BBB6F93B}")
    _methods_ = [
        comtypes.COMMETHOD([], comtypes.HRESULT, 'SetWallpaper',
            (['in'], ctypes.c_wchar_p, 'monitorID'),
            (['in'], ctypes.c_wchar_p, 'wallpaper')
        ),
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetWallpaper',
            (['in'], ctypes.c_wchar_p, 'monitorID'),
            (['out'], ctypes.POINTER(ctypes.c_wchar_p), 'wallpaper')
        ),
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetMonitorDevicePathAt',
            (['in'], ctypes.c_uint, 'index'),
            (['out'], ctypes.POINTER(ctypes.c_wchar_p), 'monitorID')
        ),
        comtypes.COMMETHOD([], comtypes.HRESULT, 'GetMonitorDevicePathCount',
            (['out'], ctypes.POINTER(ctypes.c_uint), 'count')
        ),
    ]


#Initialize COM
comtypes.CoInitialize()
wallpaper = comtypes.client.CreateObject(
    "{C2CF3110-460E-4fc1-B9D0-8A1C0C9CC4BD}",
    interface=IDesktopWallpaper
)

#Get the number of monitors connected to the system and the ID of each monitor to set the wallpaper on the correct screen.
count = wallpaper.GetMonitorDevicePathCount()

#(You can add as many monitors as you want, but for the example we will only use two monitors, one horizontal and one vertical.)
monitor0 = wallpaper.GetMonitorDevicePathAt(0)
monitor1 = wallpaper.GetMonitorDevicePathAt(1)

#Choose a random image from the folder where you have your wallpapers stored. You can change the path to the folder where you have your wallpapers.
folder = Path(r"path/to/your/wallpapers/folder")
images = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))
azar = random.choice(images)

#With this we are ensuring that there is no repetition of the wallpaper, by comparing the selected image with the one that was set as wallpaper the last time the script was run. If they are the same, it will select another random image until it finds one that is different.
with open("path/to/txt/with/name/of/previous/wallpaper.txt", "r") as f:
    fondo_anterior = f.read().strip()
    while fondo_anterior == str(azar):
        azar = random.choice(images)  # Choose another random image if it is the same as the previous one

#Write the selected image to a text file so that it can be compared the next time the script is run to avoid repetition of the wallpaper.
with open("path/to/txt/with/name/of/previous/wallpaper.txt", "w") as f:
    f.write(str(azar))

#Stablish the wallpaper in the monitor that you want, in this case we are setting it on the second monitor (monitor1), but you can change it to monitor0 if you want to set it on the first monitor.
wallpaper.SetWallpaper(monitor1, str(azar))


#IMPORTANT NOTE: You need to change the paths in the code to the correct paths on your system where you have your wallpapers stored and where you want to save the text file with the name of the previous wallpaper.
#           - Change "path/to/your/wallpapers/folder" to the actual path of the folder where you have your wallpapers stored.   
#           - Change "path/to/txt/with/name/of/previous/wallpaper.txt" to the actual path of the text file where you want to save the name of the previous wallpaper. This file will be used to avoid repetition of the wallpaper each time the script is run.
#                   *Just create a file with that name and put the name of one of your wallpapers in it to start with, so that the script can compare it the first time it is run and avoid repetition from the very beginning.
#           - You can also change the monitor where you want to set the wallpaper by changing monitor1 to monitor0 if you want to set it on the first monitor.
#          - Make sure you have the necessary permissions to read and write to the specified paths. 
#          - This script is designed to work on Windows systems, as it uses the Windows API to change the desktop wallpaper. It may not work on other operating systems.
#           - You can schedule this script to run at specific intervals using Task Scheduler on Windows to automatically change your wallpaper at regular intervals.
#       - Make sure to have the comtypes library installed in your Python environment to run this script. You can install it using pip if you don't have it already:
