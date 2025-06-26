# file: code_injection.py
def calc():
    expr = input("Enter Python expr: ")
    result = eval(expr)  # CWE-94
    print("Result:", result)

if __name__ == "__main__":
    calc()
