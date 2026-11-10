import socket
import subprocess

from protocol import recv_msg, send_msg

PORT = 2405
COMMAND_TIMEOUT = 5


def run_shell(cmd):
    # subprocess.run(cmd, shell=True, capture_output=True, text=True,
    #                errors="replace", timeout=COMMAND_TIMEOUT)
    # return the reply dict: a result, or a timeout error
    pass


def handle(conn, data):
    # data: the bytes of one message
    # parse the JSON and send exactly one reply on conn
    # broken JSON, JSON that is not a dict, or an unknown type -> bad request (never raise)
    pass


def serve_client(conn):
    # loop: recv_msg -> handle
    # recv_msg returned None: the client left, return
    pass


def main():
    # socket, SO_REUSEADDR, bind ("127.0.0.1", PORT), listen
    # for each client: serve_client(conn); a ConnectionError must not stop the server
    pass


if __name__ == "__main__":
    main()
