# pickle_loader.py
import pickle

def load_job():
    path = input("Pickle file path: ")
    # CWE-502: 直接 pickle.load → python/insecure-deserialization
    with open(path, 'rb') as f:
        job = pickle.load(f)
    print("Job loaded:", job)

if __name__ == "__main__":
    load_job()
