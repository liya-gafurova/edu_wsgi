from wsgiref.simple_server import make_server

class WebApp:
    """
    Django / FastApi / Flask ....
    """

    def __init__(self,environment, response):
        self.environment = environment
        self.response = response

    def __iter__(self):
        status = '200 OK'
        response_headers = [('Content-type', 'text/html'),]
        self.response(status, response_headers)

        yield b'<strong>Hello world!</strong>'


with make_server('', 8082, WebApp) as server:
    print('Serving on port 8082 \n'
          'Visit http://127.0.0.1:8082 \n'
          'To kill process press Control + C')
    server.serve_forever()