from __future__ import absolute_import, division, print_function

from pyusbtin.usbtin import USBtin
from pyusbtin.canmessage import CANMessage
from time import sleep
from pprint import pprint

import msvcrt

#CANMessage.load_dbc(r'example.dbc')
#pprint(CANMessage.dbc_info)

#print('\n'*2)

#engine = CANMessage(0x100)
#print(engine)

# engine.RPM = 2000
# engine.Torque = 125

# print(engine)

# brake = CANMessage(0x200)
# brake[2] = 0x15
# print(brake)

# unknown_with_data = CANMessage(0x1, [0xAA, 0xBB, 0xCC])
# print(unknown_with_data)


def log_data(msg):
    print('received {}'.format(hex(msg.mid)))
    print(msg)

print('\n'*2)

usbtin = USBtin()
usbtin.connect("COM5")
usbtin.add_message_listener(log_data)
usbtin.open_can_channel(100000, USBtin.ACTIVE)

test = CANMessage(20000, [0x11, 0x22, 0x44 ], False)

usbtin.send(test)

num = 0
done = False
while not done:




    if msvcrt.kbhit():
        done = True

usbtin.close_can_channel()
usbtin.disconnect()