#!/usr/bin/python
from urllib import urlencode
import urllib2
import gtk.gdk
import dbus

# change the these to your BT account email address
BT_LOGIN = 'your@email.com'
PASSWORD = 'password'


def login():
    url = 'https://www.btopenzone.com:8443/tbbLogon'
    data = {
        'username': BT_LOGIN,
        'password': PASSWORD
    }
    req = urllib2.Request(url, urlencode(data), {})
    resp = urllib2.urlopen(req)

    if '/accountLogoff' in resp.read():
        return True
    else:
        return False


def main():
    # using google hosted small webpage to test
    # our requests aren't being moved to BT
    try:
        resp = urllib2.urlopen('http://www.google.com/iwanta404page')
        notify('Logging you into BTWifi...')
        login_resp = login()

        if login_resp is False:
            notify('Login failed')
    except (urllib2.HTTPError, urllib2.URLError):
        # Wifi should be working
        pass


def notify(message):
    item = 'org.freedesktop.Notifications'
    path = '/org/freedesktop/Notifications'
    interface = 'org.freedesktop.Notifications'
    app_name = 'BTWifix'
    id_num_to_replace = 0
    icon = ''
    title = 'BTWifix'
    text = message
    actions_list = ''
    hint = ''
    time = 2500

    bus = dbus.SessionBus()
    notif = bus.get_object(item, path)
    notify = dbus.Interface(notif, interface)
    notify.Notify(app_name, id_num_to_replace, icon, title, text, actions_list, hint, time)


if __name__ == '__main__':
    main()