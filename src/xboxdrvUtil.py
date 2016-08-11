import os, struct, array
import sys
import ConfigParser

absmap = [
	'X1',
	'Y1',
	'X2',
	'Y2'
]

keymap = [
	'A',
	'B',
	'X',
	'Y',
	'LB',
	'RB',
	'LT',
	'RT',
	'DL',
	'DR',
	'DU',
	'DD',
	'BACK',
	'START',
	'GUIDE'
]

header = "[xboxdrv]\nsilent=true\n#deadzone=6000\ndpad-as-button=true\ntrigger-as-button=true\nmimic-xpad=true\n\n"

def PrintConfig(file, _keymap, _absmap):
	global keymap, absmap

	Config = ConfigParser.ConfigParser()
 	Config.optionxform = str

	file.write(header)

	#Config.add_section("evdev-absmap")

	#for i in range (len(absmap)):
	#	Config.set("evdev-absmap", _absmap[i], absmap[i])

	Config.add_section("evdev-keymap")
	for i in range (len(keymap)):
		Config.set("evdev-keymap", _keymap[i], keymap[i])

	Config.write(file)
