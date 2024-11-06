import http.server
import ssl

# Define the server address and port
server_address = ('localhost', 4443)

# Create a simple HTTP request handler
#built-in request handler in Python that makes it easy to serve files from a directory over HTTP
handler = http.server.SimpleHTTPRequestHandler

# Create the HTTP server
#contains the files of the desktop directory
httpd = http.server.HTTPServer(server_address, handler)

# Create an SSL context
#setting up a secure HTTPS connection

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

# Load the server's certificate and private key
#
ssl_context.load_cert_chain(certfile='/home/kali/Desktop/certificate.pem', keyfile='/home/kali/Desktop/private_key.pem')

#enables HTTPS on the server
httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

# Start the HTTPS server	Ip of the server	The port of the server
print(f"Server started on https://{server_address[0]}:{server_address[1]}")

httpd.serve_forever() #makes the server running until trunuing it of using ctrl+c
