import dbus
import helpers

bus = dbus.SessionBus()
proxy = bus.get_object("org.mpris.MediaPlayer2.rhythmbox", "/org/mpris/MediaPlayer2")
player = dbus.Interface(proxy, dbus_interface="org.mpris.MediaPlayer2.Player")
player.Pause()
# Set to the the start of playing media by specifying a large time value
player.Seek(-36000000000)
# Seek to the specified time offset
player.Seek(helpers.to_microsecs("00:05:00"))
player.Play()
