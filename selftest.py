"""Local tester for server.py and client.py - not the hidden grader.

    python3 selftest.py

Starts your server.py in the background and runs a few commands with your run_command. The last
one gets stuck on purpose, so wait a few seconds. Change the examples and try your own.
"""
import os
import socket
import subprocess
import sys
import time

HOST = "127.0.0.1"
PORT = 2405


def port_is_taken():
    try:
        socket.create_connection((HOST, PORT), timeout=1).close()
        return True
    except OSError:
        return False


def main():
    if port_is_taken():
        print(f"Something (probably a server.py you started) is already listening on port {PORT}.")
        print("Stop it with Ctrl+C in its window, then run selftest.py again.")
        sys.exit(1)
    here = os.path.dirname(os.path.abspath(__file__))
    server = subprocess.Popen([sys.executable, os.path.join(here, "server.py")], cwd=here)
    try:
        time.sleep(1)
        if server.poll() is not None:
            print("server.py stopped right after starting (its error is printed above).")
            sys.exit(1)
        sys.path.insert(0, here)
        from client import run_command

        with socket.create_connection((HOST, PORT)) as s:
            s.settimeout(15)
            for cmd in ("echo hello", "ls /nope", "exit 3", "echo abc | tr a-z A-Z", "sleep 30"):
                print(cmd, "->", run_command(s, cmd))
    finally:
        server.kill()


if __name__ == "__main__":
    main()
