# file: code_eval.py
def calc():
    expr = input("Enter expression: ")
    # CWE-94: 任意 eval
    result = eval(expr)
    print("Result:", result)

if __name__ == "__main__":
    calc()
