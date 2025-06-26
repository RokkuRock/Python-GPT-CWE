# template_injection.py
from jinja2 import Template

def render():
    tpl = input("Enter template (e.g. {{ 7*7 }}): ")
    # CWE-94: 直接用使用者輸入建立 Template
    rendered = Template(tpl).render()
    print("Output:", rendered)

if __name__ == "__main__":
    render()
