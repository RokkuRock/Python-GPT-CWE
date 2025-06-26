# yaml_load.py
import yaml

def load_config():
    path = input("YAML file path: ")
    # CWE-502: yaml.load 而非 safe_load，CodeQL 會報警
    with open(path) as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    print("Config keys:", list(cfg.keys()))

if __name__ == "__main__":
    load_config()
