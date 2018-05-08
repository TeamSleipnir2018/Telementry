import time
import os
import sys
import re
import json
import sqlite3
from digi.xbee.devices import XBeeDevice
from digi.xbee.exception import TimeoutException

if os.name == "windows" or os.name == "nt" :
    PORT = "COM" + sys.argv[1]
elif os.name == "linux" or os.name == "posix" :
    PORT = "/dev/ttyS" + sys.argv[1]
BAUD_RATE = 9600
db = sqlite3.connect("test.db")
c = db.cursor()

def main():

    print(" +------------------------+")
    print(" | Reading XBee data      |")
    print(" +------------------------+\n")

    xbee = XBeeDevice(PORT, BAUD_RATE)
    message = None

    c.execute('''
    CREATE TABLE vehicledata
    (
        rpm INTEGER,
        speed INTEGER,
        oilTemp REAL,
        waterTemp REAL,
        volt INTEGER,
        brakeTemp INTEGER
    );
    ''')

    try:
        xbee.open()
        time.sleep(1)
        message = xbee.read_data()
        print(message)
        xbee.close()
        print(message.data)
        data = json.loads(message.data[17:-3].decode("utf-8"))
        print(data)

    except TimeoutException as e:
        print(e)

if __name__ == "__main__":
    main()