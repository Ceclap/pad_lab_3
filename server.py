# Import bibliotecilor pentru pornirea serverului Web
from http.server import HTTPServer, CGIHTTPRequestHandler
# Adresa serverului și numărul portului pe care îl va 'asculta'
server_address = ('', 8080)
# Cream obiectul server Web
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
# Pornirea serverului Web
print('pornire')
httpd.serve_forever()
print('oprire')
