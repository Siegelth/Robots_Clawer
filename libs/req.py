import urllib
import ssl
import socket

import urllib.request

class req():
    def req_url(self, url):
        self.url = url
        user_agent = 'bingbot'
        req = urllib.request.Request(url, headers={'User-Agent': user_agent})
        try:
            with urllib.request.urlopen(req, context=ssl._create_unverified_context(), timeout=60) as response:
                content = response.read().decode('utf-8', errors='ignore')
        except socket.timeout:
            print("Request timed out")
            return None
        return content
    