import os
import threading
import urllib.request
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from functools import partial

def test_index_page():
    root = os.path.dirname(os.path.dirname(__file__))
    handler = partial(SimpleHTTPRequestHandler, directory=root)
    server = ThreadingHTTPServer(('localhost', 0), handler)
    port = server.server_address[1]
    thread = threading.Thread(target=server.serve_forever)
    thread.daemon = True
    thread.start()
    try:
        with urllib.request.urlopen(f'http://localhost:{port}/index.html') as resp:
            text = resp.read().decode()
            assert resp.status == 200
            assert '(o_O)' in text
    finally:
        server.shutdown()
        thread.join()
