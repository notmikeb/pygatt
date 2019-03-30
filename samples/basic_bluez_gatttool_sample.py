#!/usr/bin/env python
from __future__ import print_function

import binascii
import pygatt

YOUR_DEVICE_ADDRESS = "11:22:33:44:55:66"
YOUR_DEVICE_ADDRESS = "B0:B4:48:C9:6A:07"
# Many devices, e.g. Fitbit, use random addressing - this is required to
# connect.
ADDRESS_TYPE = pygatt.BLEAddressType.random
ADDRESS_TYPE = pygatt.BLEAddressType.public

adapter = pygatt.GATTToolBackend()
adapter.start()
device = adapter.connect(YOUR_DEVICE_ADDRESS, address_type=ADDRESS_TYPE)

cs =  device.discover_characteristics()
cs = [i for i in cs.keys()]
for uuid in cs:
    print("Read UUID %s: %s" % (uuid, binascii.hexlify(device.char_read(uuid))))
