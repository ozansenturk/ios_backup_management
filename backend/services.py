from iOSbackup import iOSbackup



def get_devices():

    devices = iOSbackup.getDeviceList()

    return devices
