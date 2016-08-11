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

	file.write("[evdev-absmap]\n")

	for i in range (len(absmap)):
		file.write(_absmap[i]+" = "+absmap[i]+"\n")

	file.write("\n")

	file.write("[evdev-keymap]\n")

	for i in range (len(keymap)):
		file.write(_keymap[i]+" = "+keymap[i]+"\n")

	file.write("\n")

	Config.write(file)
