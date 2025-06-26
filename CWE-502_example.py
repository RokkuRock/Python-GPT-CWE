# insecure_deserialize.py
import pickle

def load_object():
    path = input("Pickle file path: ")
    # CWE-502: 未驗證來源直接反序列化
    with open(path, 'rb') as f:
        obj = pickle.load(f)
    print("Loaded:", type(obj))

if __name__ == "__main__":
    load_object()
