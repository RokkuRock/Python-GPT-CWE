# xxe.py
import xml.dom.minidom

def parse_user_xml():
    fname = input("XML filename: ")
    # CWE-611: 預設啟用外部實體解析
    doc = xml.dom.minidom.parse(fname)
    print("Root element:", doc.documentElement.tagName)

if __name__ == "__main__":
    parse_user_xml()
