# dynamic_import.py
def run_plugin():
    name = input("Plugin module name: ")
    # CWE-829: 未驗證直接由 user input 呼叫 __import__
    mod = __import__(name)
    print("Loaded:", mod)

if __name__ == "__main__":
    run_plugin()
