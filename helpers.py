import re

"""
Helper functions for mpris-dbus sample code
"""


def to_microsecs(time_str: str) -> int:
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
            "Invalid time format. The valid format is HH:MM:SS."
            "The maximum value is 99:59:59."
            "The minimum value is 00:00:00"
        )
    parts = time_str.split(":")
    int_parts = [int(s) for s in parts]
    hours, mins, secs = int_parts
    total_mins = (hours * 60) + mins
    mins_in_microsecs = total_mins * 60000000
    total_microsecs = mins_in_microsecs + (secs * 1000000)
    return total_microsecs
