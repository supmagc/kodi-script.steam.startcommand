import os
import sys
import subprocess
import time
import shutil
import stat
import xbmc
import xbmcaddon
import xbmcgui


addon_id = 'script.steam.startcommand'
encoding = 'utf-8'


addon = xbmcaddon.Addon(id=addon_id)
addon_icon = addon.getAddonInfo('icon')
dialog = xbmcgui.Dialog()
language = addon.getLocalizedString


def log(msg):
	msg = msg.encode(encoding)
	xbmc.log('%s: %s' % (addon_id, msg))
    

def kodi_busy_dialog():
    xbmc.executebuiltin("ActivateWindow(busydialognocancel)")
    log('busy dialog started')
    time.sleep(5)
    xbmc.executebuiltin("Dialog.Close(busydialognocancel)")
    log('busy dialog stopped')


if __name__ == '__main__':
    cmd = "htpcinit-steam open"
    try:
        log('attempting to launch: %s' % cmd)
        print cmd.encode(encoding)
        subprocess.Popen(cmd.encode(encoding), shell=True, close_fds=True)
        kodi_busy_dialog()
    except:
        log('ERROR: failed to launch: %s' % cmd)
        print cmd.encode(encoding)
        dialog.notification(language(59212), language(59215), addon_icon, 5000)