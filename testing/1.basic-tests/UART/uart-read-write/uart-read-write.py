# This example will test our Product's serial interface
#
# The goal of this example is to show you how you can read and write data from/to
# your device using the serial interface, and how you can assert string and byte
# values.
#
# If you want to replicate this setup, serial interface is available via the
# Testboard's TX and RX pins. To use them to communicate with your Product,
# connect the TX pin to your device's RX pin, the RX to your device's TX pin,
# and the ground to your device's ground.
#
# Please take into account that the voltage levels on these pins operate at 0V to
# 3.3V and should not be connected directly to a computer's RS232 serial port which
# operates at +/- 12V and will damage the Testboard.
#
# Also note that for the serial channel configuration, it is possible to specify
# the baud rate, the number of data bits, stop bits, parity, flow control and other
# settings.
#

import time
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("Tester2")


#
# Setup the serial interface
#
def serial_config():
    Serial = Testboard.Serial
    # Configure serial interface (baudrate and config, where config:
    # data bits | stop bits | parity | hw flow control | LIN configuration
    testboard.serialSetup(9600, Serial.DATA_BITS_8 | Serial.STOP_BITS_1 | Serial.PARITY_NO)


#
# Validate device TX by writing a series of bytes from device to testboard
#
def validate_serial_TX_data():

    buffer = ''
    end_of_buff = False

    spanner.assertEqual("Hello Testboard\n", "Hello Testboard\n")

    print("Waiting for handshake")

    while not end_of_buff:
        data_length = testboard.serialAvailable()
        print("Available chars: " + str(data_length))

        # Read the requested bytes from testboard's serial
        while data_length > 0:
            new_char = testboard.serialReadByte().decode('ascii')
            buffer += new_char
            data_length -= 1
            if new_char == '\n':
                end_of_buff = True
                break

    print("Received Buffer " + buffer)

    # Check if we received the requested bytes in testboard
    spanner.assertEqual("Hello Testboard\n", buffer)

    # Send to device
    testboard.serialWrite("Hello device\n")


#
# Validate device TX by writing one byte from device to testboard and echoing
# back the data to the device.
#
def validate_serial_TX_echo_back():
    # Read one byte from testboard's serial
    value = testboard.serialReadByte()

    # Check if we received the requested byte in the testboard
    spanner.assertEqual(b'\x31', value)

    # Write one byte to the device
    testboard.serialWrite(value)


if __name__ == "__main__":

    serial_config()

    time.sleep(2)

    validate_serial_TX_data()

    time.sleep(2)

    validate_serial_TX_echo_back()
    