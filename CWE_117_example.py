# log_injection.py
import logging

logging.basicConfig(filename="events.log", level=logging.INFO)

def record_event():
    evt = input("Event: ")
    # CWE-117: 未淨化即可寫入日誌，可能插入偽造條目
    logging.info(evt)
    print("Event recorded")

if __name__ == "__main__":
    record_event()
