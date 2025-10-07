import socket, sys


def scan_port(host: str, port: int) -> str:
    """Returns a string status of the queried host:port"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1.0)
    try:
        s.connect((host, port))
        return "OPEN"
    except socket.timeout:
        return "TIMEOUT"
    except ConnectionRefusedError:
        return "CLOSED"
    except Exception as e:
        return f"{e}"
    finally:
        s.close()

def main(argv) -> int:
    """Terminal entrypoint. Returns exit code 0 = success, 1 = input error."""
    if len(argv)!=3:
        print("error: scanner.py takes 2 arguments <host> <port>")
        return 2
    host = argv[1] # Lav noget host = resolve_address(argv[1])
    try:
        port = int(argv[2])
    except ValueError:
        print("Port must be an integer in range 0-65535")
        return 2
    
    try:
        status = scan_port(host, port)
        print(f"{host}:{port} {status}")
        return 0
    except KeyboardInterrupt:
        print("Interrupted by user.")
        return 2

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))