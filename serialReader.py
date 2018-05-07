import time
import os
import serial
from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import TimeoutException

print(os.name)

if os.name == "windows" or os.name == "nt" :
    PORT = "COM7"
elif os.name == "linux" or os.name == "posix" :
    PORT = "/dev/ttyS7"
BAUD_RATE = 9600

def main():

    print(" +------------------------+")
    print(" | Reading XBee data      |")
    print(" +------------------------+\n")

    xbee = XBeeDevice(PORT, BAUD_RATE)
    message = None

    try:
        xbee.open()
        time.sleep(1)
        message = xbee.read_data()
        xbee.close()
        print(message.data)

    except TimeoutException as e:
        print(e)

if __name__ == "__main__":
    main()