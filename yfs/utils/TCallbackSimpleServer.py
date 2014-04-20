import socket


'''
    This simple wrapper, is just invoke the handler "up" method and say -
    "We are serving requests.. on this ip and port"
'''


class TCallbackSimpleServer:
    def __init__(self, server, handler):
        self._server = server
        self._handler = handler

    def serve(self):
        ip = socket.gethostbyname(socket.gethostname())
        port = self._server.serverTransport.port

        self._handler.up(ip, port)
        self._server.serve()