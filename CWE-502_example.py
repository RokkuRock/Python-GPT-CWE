# file: insecure_deserialize.py
import pickle

def load_data():
    fname = input("Pickle filename: ")
    # CWE-502: 未驗證來源直接反序列化
    with open(fname, 'rb') as f:
        data = pickle.load(f)
    print("Loaded object:", data)

if __name__ == "__main__":
    load_data()
