# This example will toggle one of our device's inputs, which will respond
# accordingly by sending a network command, to showcase a product's actual usage.
#
# In this particular example the device we are testing is a Water Flooding
# Alarm, which responds by sending an "alarm_triggered" command with a value of
# "water" when the water flooding sensor pin is triggered.

# The goal of this example is to show you how you can receive network commands
# to your devices through the AWS device communication infrastructure, after
# setting one of the device's environmental inputs.
#
# This is one real world example of a very simple functional test you would run
# for your devices.

import time
import spanner
import Device from AWSDevice
import Testboard


device = Device("device_name")

testboard = Testboard("testboard_name")

# Our Product's Input will be connected the Testboard's Pin D3, making it our
# Output Pin
OUTPUT_PIN = "D3"


def test_raise_flooding_alarm():
    # set PIN state
    testboard.digitalWrite(OUTPUT_PIN, HIGH)

    time.sleep(2)

    # Ask spanner to wait for 3 seconds while at the same time checking if we
    # got a command from the device
    result = device.waitForCommand(3)

    # Make sure we actually got a command, and we didn't just time out
    spanner.assertTrue(result.commandReceived)
    # Double check the name of the command
    spanner.assertEqual("alarm_triggered", command.name)
    spanner.assertEqual("water_flooding", command.value)


if __name__ == "__main__":

    spanner.runTest(test_raise_flooding_alarm())


# NOT READY
