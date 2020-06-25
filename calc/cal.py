from cgi import parse_qs, escape
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    
    x = d.get('x', [''])[0]
    y = d.get('y', [''])[0]

    Sum = 0
    Product = 0
    
    if '' not in [x, y]:
        x, y = int(x), int(y)
        Sum = x+y
        Product = x*y
        
    response_body = html%{
        'Sum' : Sum,
        'Product' : Product
        }
    
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]
    
    start_response(status, response_headers)
    return [response_body]