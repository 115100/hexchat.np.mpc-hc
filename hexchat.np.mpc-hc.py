# Inspired by https://github.com/mpc-hc/snippets
from bs4 import BeautifulSoup
import hexchat
import requests

__module_name__ = 'MPC-HC Now Playing'
__module_version__ = '0.3.1'
__module_description__ = 'MPC-HC Now Playing script'


def now_playing(*_):

    try:
        resp = requests.get('http://127.0.0.1:13579/info.html')
        resp.raise_for_status()
    except requests.exceptions.HTTPError:
        hexchat.prnt('Nothing open in MPC-HC')
        return

    soup = BeautifulSoup(resp.text)

    hexchat.command('SAY np: ' + soup.p.string)

    return hexchat.EAT_ALL


def unload_callback(_):
    hexchat.prnt('RIP np script')

hexchat.hook_command('mpc',
                     now_playing,
                     help='"/mpc" to display currently playing MPC-HC media')
hexchat.hook_unload(unload_callback)
hexchat.prnt('hexchat.np.mpc-hc.py loaded')
