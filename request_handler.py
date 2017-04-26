"""Holds a simple webserver with a custom request handler for our Diversifier."""
import cgi
from urllib import parse
from http.server import BaseHTTPRequestHandler, HTTPServer

from strdiver.diversifier import Diversifier

class MyHttpRequestHandler(BaseHTTPRequestHandler):
    """A request handler which calls the Diversifier for GET and POST calls."""

    def _set_headers(self, code=200):
        self.send_response(code)
        self.send_header('Content-type', 'json')
        self.end_headers()

    def do_GET(self):
        """
            We respond with 200 and the json-data from diversify,
            if we got the correct url and the necessary param.
            Else we respond with a code 400.
        """
        urlsplit = parse.urlsplit(self.path)

        if urlsplit.path == "/diversify":
            params = parse.parse_qs(urlsplit.query)

            if "value" in params:
                self._set_headers()
                value = params["value"][0]
            else:
                self._set_headers(400)
                return

            output = get_json_output(value)
            self.wfile.write(output.encode())
        else:
            self._set_headers(400)

    def do_POST(self):
        """
            We respond with 200 and the json-data from diversify,
            if we got necessary form data.
            Else we respond with a code 400.
        """
        self._set_headers()
        ctype, pdict = cgi.parse_header(self.headers['content-type'])
        pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

        if ctype == 'multipart/form-data':
            postvars = cgi.parse_multipart(self.rfile, pdict)
        else:
            postvars = {}

        if "value" in postvars:
            self._set_headers()
            value = str(postvars["value"][0], 'utf-8')
        else:
            self._set_headers(400)
            return

        output = get_json_output(value)
        self.wfile.write(output.encode())

def get_json_output(value):
    """Uses the Diversifier to aggregate a respond json for us."""
    diversifier = Diversifier(value)
    return diversifier.aggregate()


def run(server_class=HTTPServer, handler_class=MyHttpRequestHandler, port=80):
    """Starts a server with our custom handler."""
    server_address = ('0.0.0.0', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd, gimme requests...')
    print('Listening on localhost:' + str(port))
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
