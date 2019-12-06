import requests
from carrencyImport import *
from telega import Telega
import schedule
import time


def main():
    t = Telega("981624897:AAFD1wu7bBI4XCR3JHvf9iYqRLPZujpDLJM")

    # Уровни отслеживания
    usdrur = 63.50
    eurusd=1.1100

    curency_dic = currency_import()


    if curency_dic["usdrur"] < usdrur:
        t.send_message(t.chat_id(), "Пара USD/RUR опустилась ниже 63.5" )
        t.send_message(t.chat_id(), curency_message(currency_import()))

    if curency_dic["eurusd"] > eurusd:
        t.send_message(t.chat_id(), "Пара EUR/USD поднялась выше 1.1100" )
        t.send_message(t.chat_id(), curency_message(currency_import()))
        usdrur = 0




if __name__ == "__main__":
    schedule.every(32).minutes.do(main)

    while True:
        schedule.run_pending()
        time.sleep(1)
