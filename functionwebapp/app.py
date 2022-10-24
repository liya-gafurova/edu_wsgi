from wsgiref.simple_server import make_server


def web_app(environment, response):
    for env, val in environment.items():
        print(f'{env}: {val}')

    print(type(response))

    status = '200 Ok'
    headers = [('Content-type', 'text/html')]
    response(status, headers)

    return [b'<strong>Hello world! Function based WSGI</strong>']


with make_server('', 8082, web_app) as server:
    print('Serving on port 8082 \n'
          'Visit http://127.0.0.1:8082 \n'
          'To kill process press Control + C')
    server.serve_forever()