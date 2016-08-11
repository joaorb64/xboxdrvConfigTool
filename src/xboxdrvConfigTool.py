import evdev
import os, struct, array
import sys
import subprocess
import signal
import time
from evdev import InputDevice, categorize, ecodes, util, AbsInfo
import xboxdrvUtil

def ReadInput(device):
	for event in device.read_loop():
		if event.type == ecodes.EV_KEY:
			scancode = evdev.events.KeyEvent(event).scancode

			if(evdev.events.KeyEvent(event).keystate == 1):
					return("KEY_#"+str(scancode))
				#if(isinstance(keycode, list)):
				#		return(keycode[0])
				#else:
				#		return(keycode)

		if event.type == ecodes.EV_ABS:
			evtypes = device.capabilities(verbose=True, absinfo=True)
			maxx = 0
			minn = 0
			
			for ev in evtypes:
				if(ev[0] == "EV_ABS"):
					for abss in evtypes[ev]:
						if(abss[0][0] == evdev.ecodes.ABS[event.code]):
							maxx = abss[1].max
							minn = abss[1].min
			
			normval = (float(event.value+abs(minn))/float(maxx-minn))*2.0-1.0
			#print("val: "+str(event.value)+" - min: "+str(minn)+" - max: "+str(maxx)+" - normalized: "+str(normval))

			if(abs(normval) > 0.5):
				return(evdev.ecodes.ABS[event.code])

def Configure():
	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

	for i in range(0, len(devices)):
		print(str(i)+' - '+devices[i].name+'('+devices[i].fn+', '+devices[i].phys+')')

	devId = input ('Select device id: ')

	device = devices[devId]

	keyremap = []

	for i in range (len(xboxdrvUtil.keymap)):
		print("Button for "+xboxdrvUtil.keymap[i]+": ")
		press = ReadInput(device)
		print(press)
		keyremap.append(press)

	absremap = []

	for i in range (len(xboxdrvUtil.absmap)):
		print("Axis for "+xboxdrvUtil.absmap[i]+": ")
		press = ReadInput(device)
		print(press)
		absremap.append(press)

	cfgfile = open((device.name).replace(" ", ""),'w')

	xboxdrvUtil.PrintConfig(cfgfile, keyremap, absremap)

	cfgfile.close()

	print("\nSaved as: "+cfgfile.name+"\n")

def Launch():
	devices = [evdev.InputDevice(fn) for fn in evdev.list_devices()]

	for i in range(0, len(devices)):
		print(str(i)+' - '+devices[i].name+'('+devices[i].fn+', '+devices[i].phys+')')

	devId = input ('Select device id: ')

	device = devices[devId]

	command = 'xboxdrv --evdev '+device.fn+' -c '+(device.name).replace(" ", "")
	print(command)
	subprocess.call(command, shell=True)

def main():
	while True:
		print("\n")
		print("***********************")
		print("* XBOXDRV CONFIG TOOL *")
		print("***********************")
		print("1 - Configure a controller")
		print("2 - Run xboxdrv for a controller")
		print("Anything else - Quit\n")
		option = raw_input("Option: ")

		if option == "1":
			Configure()
		elif option == "2":
			Launch()
		else:
			break

main()
