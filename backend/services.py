from iOSbackup import iOSbackup



def get_devices():

    try:
        devices = iOSbackup.getDeviceList()
    except Exception as e:
        print("error {}".format(e))
        devices = []

    return devices
