# pickle_deserialize.py
import pickle, socket

def load_remote():
    # 從簡易 TCP 服務讀取序列化資料
    s = socket.socket()
    s.bind(('localhost', 9000))
    s.listen(1)
    conn, _ = s.accept()
    data = conn.recv(4096)
    # CWE-502: 直接 pickle.loads 未驗證來源
    obj = pickle.loads(data)
    print("Received:", obj)

if __name__ == "__main__":
    load_remote()
