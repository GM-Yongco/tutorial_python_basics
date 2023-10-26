# Description     : Code that will impress u ;)
# Author          : G.M. Yongco #BeSomeoneWhoCanStandByShinomiya
# Date            : ur my date uwu
# HEADERS ================================================================

# most of windows is in c and we need these typesto interact with it
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

# pycaw stands for python core audio windows
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume

# ========================================================================
# FUNCTIONS 1
# ========================================================================

def set_master(vol_level = 0):
	print(vol_level)
	
	# getting the volume of the full speakers
	devices = AudioUtilities.GetSpeakers()
	# gets the interface
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	# gets the volume handler
	volume = cast(interface, POINTER(IAudioEndpointVolume))
	
	volume.SetMasterVolumeLevel(vol_level, None)
	# note: the range is in (0, -65) inclusive, 
	# which is in weird decibel notation
	# with 0 being vol 100 and -65 being 0

	# and with some testing, found -10 to be 51

def master_volume():
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))

	return volume

def set_master_mute():
	volume = master_volume()

	# basically uses a boolean to set if mute
	volume.SetMute(1, None)

def set_master_unmute():
	volume = master_volume()

	volume.SetMute(0, None)

def print_current_volume():
	volume = master_volume()

	# also uses the weir decibel thingy
	current = volume.GetMasterVolumeLevel()
	print(current)
	

# ========================================================================
# FUNCTIONS 2
# ========================================================================

def print_sessions():
	sessions = AudioUtilities.GetAllSessions()

	for session in sessions:
		if session.Process:
			print(session.Process.name())

def get_session(name = "Spotify.exe"):
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		if session.Process and (session.Process.name() == name):
			volume =  session._ctl.QueryInterface(ISimpleAudioVolume)
			return volume

def set_session_volume(vol_level = 0.5):
	volume = get_session()
	volume.SetMasterVolume(vol_level, None)

def get_session_volume():
	volume = get_session()
	current = volume.GetMasterVolume()

	print(current)

def set_sesssion_mute():
	volume = get_session()
	volume.SetMute(1, None)

def set_sesssion_unmute():
	volume = get_session()
	volume.SetMute(0, None)

def set_sesssion_mute_dynamic():
	volume = get_session()
	if volume.GetMute():
		volume.SetMute(0, None)
	else:
		volume.SetMute(1, None)

# ========================================================================
# FUNCTIONS 3
# ========================================================================

def find_application_volume(name):
	devices = AudioUtilities.GetSpeakers()
	interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
	volume = cast(interface, POINTER(IAudioEndpointVolume))
	sessions = AudioUtilities.GetAllSessions()
	for session in sessions:
		if session.Process and session.Process.name() == name:
			return volume, session

# ========================================================================
# MAIN 
# ========================================================================

def main():
	# set_session_volume()
	set_sesssion_mute_dynamic()

if __name__ == '__main__':
	print("\nSTART ----------------------------------------")
	main()

	print("\nEND ------------------------------------------")