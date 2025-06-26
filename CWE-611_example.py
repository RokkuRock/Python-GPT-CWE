# file: xxe.py
import xml.etree.ElementTree as ET

def parse_xml():
    fname = input("XML filename: ")
    # CWE-611: 預設允許外部實體
    tree = ET.parse(fname)
    root = tree.getroot()
    print("Root tag:", root.tag)

if __name__ == "__main__":
    parse_xml()
