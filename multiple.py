from concurrent.futures import ThreadPoolExecutor as PoolExecutor
import http.client
import socket

def get_it(url):
    try:
        # always set a timeout when you connect to an external server
        connection = http.client.HTTPSConnection(url, timeout=2)

        connection.request("GET", "/")

        response = connection.getresponse()

        return response.read()
    except socket.timeout:
        # in a real world scenario you would probably do stuff if the
        # socket goes into timeout
        pass

urls = [
    "www.google.com",
    "www.youtube.com",
    "www.wikipedia.org",
    "www.reddit.com",
    "www.httpbin.org"
] * 10

with PoolExecutor(max_workers=4) as executor:
    for _ in executor.map(get_it, urls):
        pass
