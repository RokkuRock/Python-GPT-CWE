# pickle_server.py
import pickle, socket

def run():
    s = socket.socket(); s.bind(('localhost', 9003)); s.listen(1)
    conn, _ = s.accept()
    data = conn.recv(4096)
    # CWE-502: 未驗證來源直接反序列化
    obj = pickle.loads(data)
    print("Loaded:", obj)

if __name__ == "__main__":
    run()
