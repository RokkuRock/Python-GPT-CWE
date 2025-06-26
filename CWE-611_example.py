# xxe.py
from xml.etree import ElementTree

def parse_xml():
    fname = input("XML file: ")
    # CWE-611: ET.parse 預設啟用外部實體
    tree = ElementTree.parse(fname)
    root = tree.getroot()
    print("Root tag:", root.tag)

if __name__ == "__main__":
    parse_xml()
