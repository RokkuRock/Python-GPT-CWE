# code_eval.py
def simple_calc():
    expr = input("Enter arithmetic expression: ")
    # CWE-94: 任意 eval，可執行惡意程式碼
    result = eval(expr)
    print("Result:", result)

if __name__ == "__main__":
    simple_calc()
