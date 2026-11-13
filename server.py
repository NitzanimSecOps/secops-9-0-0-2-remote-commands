"""The server: answers requests from clients.

Two kinds of functions:
  * BUILD A REPLY: take values, RETURN a dict. They never touch the socket.
        run_shell
  * TALK TO THE CLIENT: take conn first, SEND on it.
        handle, serve_client
"""
import json
import socket
import subprocess

from protocol import recv_msg, send_json, send_msg

PORT = 2405
COMMAND_TIMEOUT = 5


def error(message: str) -> dict:
    return {"type": "error", "message": message}


# ============================================================
#  BUILD A REPLY  (return a value, never send)
# ============================================================

def run_shell(cmd: str) -> dict:
    try:
        # TODO: subprocess.run(cmd, shell=True, capture_output=True, text=True,
        #                      errors="replace", timeout=COMMAND_TIMEOUT)
        pass
    except subprocess.TimeoutExpired:    # ran longer than COMMAND_TIMEOUT seconds
        return error("timeout")
    # TODO: return the result dict (stdout, stderr, exit_code)


# ============================================================
#  TALK TO THE CLIENT  (conn first, send on it)
# ============================================================

def handle(conn: socket.socket, data: bytes) -> None:
    # data: the bytes of one message. Send exactly one reply on conn, never raise.
    try:
        request = json.loads(data)
    except ValueError:                   # not JSON at all
        send_json(conn, error("bad request"))
        return
    # TODO: JSON that is not a dict, or an unknown type -> bad request
    # TODO: exec -> send_json(conn, run_shell(cmd))


def serve_client(conn: socket.socket) -> None:
    # loop: recv_msg -> handle
    # recv_msg returned None: the client left, return
    pass


def main() -> None:
    # socket, SO_REUSEADDR, bind ("127.0.0.1", PORT), listen, then for each client:
    #     with conn:
    #         try:
    #             serve_client(conn)
    #         except ConnectionError:   # the client vanished mid-message: wait for the next one
    #             pass
    pass


if __name__ == "__main__":
    main()
