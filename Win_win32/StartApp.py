
# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADER ------------------------------------------------------------------------------------------
from subprocess import run
import os

# MAIN --------------------------------------------------------------------------------------------
print("\nSTART ----------------------------------\n")

path = ""

if os.path.exists(os.environ['appdata'] + "\\Spotify\\Spotify.exe"):
	path += os.environ['appdata'] + "\\Spotify\\Spotify.exe"
elif os.path.exists(os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"):
	path += os.environ['localappdata'] + "\\Microsoft\\WindowsApps\\Spotify.exe"
else:
	raise ImportError("Spotify not Found.")

run([path])

print("\nEND ------------------------------------\n")