import dbus

for service in dbus.SessionBus().list_names():
    if "org.mpris" in service:
        print(service)
