# xxe_parser.py
from xml.dom.minidom import parse

def parse_user_xml():
    path = input("XML filepath: ")
    # CWE-611: DOM parser預設啟用外部實體 → python/xml-external-entity
    doc = parse(path)
    print("Root element:", doc.documentElement.tagName)

if __name__ == "__main__":
    parse_user_xml()
