"""The client: sends requests to the server and reads the replies."""
import socket
import sys

from protocol import recv_json, send_json

PORT = 2405


# ============================================================
#  TALK TO THE SERVER  (sock first)
# ============================================================

def run_command(sock: socket.socket, cmd: str) -> dict | None:
    # send an exec request, return the server's reply as a dict (None if the connection closed)
    pass


# ============================================================
#  THE COMMAND LOOP
# ============================================================

def main() -> None:
    try:
        sock = socket.create_connection(("127.0.0.1", PORT))
    except ConnectionRefusedError:
        print(f"no server on port {PORT}: start server.py first")
        return
    with sock:
        while True:
            # read a line -> run_command -> print stdout / stderr (or the error message), until exit
            # run_command returned None: the server closed the connection, stop
            pass


if __name__ == "__main__":
    main()
