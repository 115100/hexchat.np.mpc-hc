# Inspired by https://github.com/mpc-hc/snippets
import urllib2
import hexchat
import re

__module_name__ = 'MPC-HC Now Playing'
__module_version__ = '0.3'
__module_description__ = 'MPC-HC Now Playing script'

def now_playing(word, word_eol, userdata):
	try:
		page = urllib2.urlopen('http://127.0.0.1:13579/info.html').read()
	except:
		hexchat.prnt('Nothing open in MPC-HC')
		return
	line = re.search('&laquo;\s(.*?)\s&bull;\s(.*?)\s\&bull;\s(.*?)\s&bull;\s(.*?)\s&raquo;', page)
	try:
		if word[1] == 'v' or word[1] == 'full':
			hexchat.command('SAY np: {1} @ {2}, {3} with {0}'.format(line.group(1), line.group(2), line.group(3), line.group(4)))
		else:
			hexchat.command('SAY np: '+line.group(2))
	except IndexError:
		hexchat.command('SAY np: '+line.group(2))
	return hexchat.EAT_ALL;

def unload_callback(userdata):
	hexchat.prnt('RIP np script')

hexchat.hook_command('np', now_playing, help='"/np" to display currently playing MPC-HC media')
hexchat.hook_unload('unload_callback')
hexchat.prnt('hexchat.np.mpc-hc.py loaded')