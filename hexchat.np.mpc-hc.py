# Inspired by https://github.com/mpc-hc/snippets
import re

import hexchat
import requests

__module_name__ = 'MPC-HC Now Playing'
__module_version__ = '0.3.1'
__module_description__ = 'MPC-HC Now Playing script'


def now_playing(*_):

    try:
        page = requests.get('http://127.0.0.1:13579/info.html').text
    except:
        hexchat.prnt('Nothing open in MPC-HC')
        return

    line = re.search('&laquo;\s(.*?)\s&bull;'
                     '\s(.*?)\s\&bull;\s(.*?)'
                     '\s&bull;\s(.*?)\s&raquo;', page)

    hexchat.command('SAY np: '+line.group(2))

    return hexchat.EAT_ALL


def unload_callback(_):
    hexchat.prnt('RIP np script')

hexchat.hook_command('mpc',
                     now_playing,
                     help='"/mpc" to display currently playing MPC-HC media')
hexchat.hook_unload(unload_callback)
hexchat.prnt('hexchat.np.mpc-hc.py loaded')
