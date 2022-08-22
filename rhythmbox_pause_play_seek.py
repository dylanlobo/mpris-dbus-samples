import dbus
import re

def to_microsecs(time_str):
    """Converts time specified by the string HH:MM:SS into microseconds.

    Arguments
    time_str is a string.  The maximum value is 99:59:59. The minimum value is 00:00:00
    Returns
    An interger value of the converted time in microseconds
    """

    # Setup the regex expression that will validate the time format
    m = re.search("^[0-9][0-9]:[0-5][0-9]:[0-5][0-9]$", time_str)
    if m is None:
        raise ValueError(
            "Invalid time format. The valid format is HH:MM:SS."\
            "The maximum value is 99:59:59." \
            "The minimum value is 00:00:00"
        )
    parts = time_str.split(":")
    int_parts = [int(s) for s in parts]
    hours, mins, secs = int_parts
    total_mins = (hours * 60) + mins
    mins_in_microsecs = total_mins * 60000000
    total_microsecs = mins_in_microsecs + (secs * 1000000)
    return total_microsecs

bus = dbus.SessionBus()
proxy = bus.get_object("org.mpris.MediaPlayer2.rhythmbox","/org/mpris/MediaPlayer2")
player = dbus.Interface(proxy,dbus_interface="org.mpris.MediaPlayer2.Player")
player.Pause()
#Set to the the start of playing media by specifying a large time value
player.Seek(-36000000000)
#Seek to the specified time offset
player.Seek(to_microsecs("00:05:00"))
player.Play()


