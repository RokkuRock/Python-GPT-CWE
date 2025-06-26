# pickle_deserialize.py
import pickle

def load_task():
    path = input("Pickle file path: ")
    # CWE-502: 未檢查來源直接反序列化
    with open(path, "rb") as f:
        task = pickle.load(f)
    print("Loaded task:", task)

if __name__ == "__main__":
    load_task()
