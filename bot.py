import requests
from carrencyImport import *
from telega import Telega
import schedule
import time


def main():
    t = Telega("981624897:AAFD1wu7bBI4XCR3JHvf9iYqRLPZujpDLJM")
    usdrur = 63.50

    curency_dic = currency_import()

    if curency_dic["usdrur"] > usdrur:
        t.send_message(t.chat_id(), curency_message(currency_import()))


if __name__ == "__main__":
    schedule.every(10).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
