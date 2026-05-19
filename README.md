# Windows single monitor wallpaper changer
This script is meant to help you customize your PC. It will change the wallpaper of only ONE monitor of your preference. So if you have more than one monitor, and want to change one wallpaper periodically while maintaining the wallpaper of the other monitor, this script will help you with that.
## Requirements
``` 
pip install comtypes
```
Also we will be using:
- ctypes
- random
- pathlib 

## Installation
Download the script and put it into de windows task scheduler according to your needs

## Configuration
Change these variables with your own data:
- `WALLPAPERS_FOLDER` - Path to the folder where your wallpapers are stored
- `MONITOR_INDEX` - Index of the monitor you want to change (0 = first monitor, 1 = second monitor; you can add as many monitors as you want)
- `LAST_WALLPAPER_FILE` (called `previous_wallpaper` within the file) - Path to the txt file that stores the last wallpaper used
  
## Usage
Just install it and execute it within the task Scheduler. Configure it as "Run whether user is logged on or not" to avoid any CMD ugly showings
