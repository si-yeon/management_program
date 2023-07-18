import atexit

from server.controller.controller_server import ServerController

if __name__ == "__main__":
    server = ServerController()
    server.start()
    atexit.register(server.end)