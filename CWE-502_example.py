# pickle_server.py
import socket, pickle

def run_server():
    s = socket.socket()
    s.bind(('localhost', 9002))
    s.listen(1)
    conn, _ = s.accept()
    data = conn.recv(4096)
    # CWE-502: 直接 pickle.loads 未驗證來源
    obj = pickle.loads(data)
    print("Loaded:", obj)

if __name__ == "__main__":
    run_server()
