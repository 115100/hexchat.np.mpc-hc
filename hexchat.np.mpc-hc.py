# Inspired by https://github.com/mpc-hc/snippets
import urllib2
import hexchat

__module_name__ = 'MPC-HC Now Playing'
__module_version__ = '0.2'
__module_description__ = 'MPC-HC Now Playing script - Filename only'

def now_playing(word, word_eol, userdata):
	try:
		page = urllib2.urlopen('http://127.0.0.1:13579/info.html').read()
		line = page[page.find('&bull; ')+7:]
		line = line[:line.find('&bull;')]
		hexchat.command("SAY np: "+line)
	except:
		hexchat.prnt("Nothing open in MPC-HC")
	return hexchat.EAT_ALL;

hexchat.hook_command('np', now_playing, help='"/np" to display currently playing MPC-HC media')
hexchat.prnt('hexchat.np.mpc-hc.py loaded')