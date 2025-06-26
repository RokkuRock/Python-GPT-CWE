# yaml_deserialize.py
import yaml

def load_config():
    fname = input("YAML config file path: ")
    # CWE-502: 使用 yaml.load 而非 safe_load
    with open(fname) as f:
        cfg = yaml.load(f, Loader=yaml.FullLoader)
    print("Config:", cfg)

if __name__ == "__main__":
    load_config()
