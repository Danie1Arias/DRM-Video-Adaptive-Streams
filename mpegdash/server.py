from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

port = 4443
httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
sslctx.check_hostname = False # If set to True, only the hostname that matches the certificate will be accepted
sslctx.load_cert_chain(certfile='server.pem', keyfile="server.pem")
httpd.socket = sslctx.wrap_socket(httpd.socket, server_side=True)
print(f'Starting server on port {port}')
httpd.serve_forever()