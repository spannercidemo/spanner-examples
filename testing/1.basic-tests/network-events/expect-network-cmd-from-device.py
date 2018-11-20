# This example will expect a command from our device, as it should send during
# a product's actual usage
#
# The goal of this example is to show you how you can expect a network command
# from your devices through the AWS device communication infrastructure.
#
# In our particular example, we are only waitinf for a "heartbeat" command which
# should happen every two seconds, so we should definitely get one if we wait
# for 3. Of course this would never be a real world example, it's only for
# educational purposes

import time
import json
import pprint
import sseclient
import os

particle_token = os.environ['PARTICLE_TOKEN']

def with_urllib3(url):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False)

def expect_network_cmd():

    url = 'https://api.particle.io/v1/devices/events?access_token='+particle_token
    response = with_urllib3(url)  # or with_requests(url)
    client = sseclient.SSEClient(response)
    # acts like a while loop
    for event in client.events():
        data = json.loads(event.data)
        # e.g data['data'] = 'turned_on'
        # when event arrives fire spanner.assertEqual
        spanner.assertEqual("turned_on", data['data'])


if __name__ == "__main__":

    expect_network_cmd()


# NOT READY
