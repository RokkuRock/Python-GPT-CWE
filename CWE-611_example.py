# xxe_parser.py
from xml.etree import ElementTree

def parse():
    fname = input("XML file: ")
    # CWE-611: ET.parse 預設允許外部實體
    tree = ElementTree.parse(fname)
    print("Root:", tree.getroot().tag)

if __name__ == "__main__":
    parse()
