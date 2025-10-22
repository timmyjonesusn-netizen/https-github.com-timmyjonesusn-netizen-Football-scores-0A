# run.py — launcher for TimmyApp (no f-strings, iOS-friendly)
import socket, threading, time, webbrowser, random
from serv_timmyapp import create_app

def find_open_port(start=5000, limit=20):
    port = start
    for _ in range(limit):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.bind(("127.0.0.1", port))
            s.close()
            return port
        except OSError:
            port += 1
    return random.randint(6000, 9000)

def auto_open(url):
    time.sleep(1)
    try:
        webbrowser.open(url)
    except Exception:
        pass

if __name__ == "__main__":
    app = create_app()
    port = find_open_port()
    url = "http://127.0.0.1:" + str(port) + "/"
    t = threading.Thread(target=auto_open, args=(url,))
    t.daemon = True
    t.start()
    app.run(host="127.0.0.1", port=port, debug=False)
