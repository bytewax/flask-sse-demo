import json

import sseclient
import urllib3

def open_stream(url, headers):
    """Get a streaming response for the given event feed using urllib3."""
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False, headers=headers)

if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/stream'
    headers = {'Accept': 'text/event-stream'}
    response = open_stream(url, headers)
    client = sseclient.SSEClient(response)
    stream = client.events()

    while True:
        event = next(stream)
        print(f"event: {event.event} \ndata: {event.data}\nevent_id:{event.id}")