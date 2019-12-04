import requests
from bs4 import BeautifulSoup


def currency_import():
    url = "http://quote-spy.com/"
    cookie = {"Quotes_MarketsOpen": "-1808833627:|:-483653703:|:746084530"}
    r = requests.get(url, cookies=cookie)
    # print(r.text)
    try:
        soup = BeautifulSoup(r.content, "lxml")
        # print(soup.text)
        usdrur = soup.find("td", id="CurrenciesUSD/RUBPrice").text.strip()
        if "," in usdrur:
            usdrur = float(usdrur.replace(",", "."))
        eurusd = soup.find("td", id="CurrenciesEUR/USDPrice").text.strip()
        if "," in eurusd:
            eurusd = float(eurusd.replace(",", "."))

        brent = soup.find("td", id="ЭнергоресурсыBrentPrice").text.strip()
        if "," in brent:
            brent = float(brent.replace(",", "."))
        gold = soup.find("td", id="МеталлыGoldPrice").text.strip().split()
        gold = gold[0] + gold[1]
        if "," in gold:
            gold = float(gold.replace(",", "."))
    except:
        print("except")
        usdrur = ""
        eurusd = ""
        brent = ""
        gold = ""
    # print(usdrur,eurusd,brent,gold)
    return {"usdrur": usdrur, "eurusd": eurusd, "brent": brent, "gold": gold}
    # print(usdrur,eurusd,brent,gold)


def curency_message(dic):
    bot_message = "USD/RUR    {}\n\
EUR/USD    {}\n\
BRENT        {}\n\
GOLD          {}".format(dic["usdrur"], dic["eurusd"], dic["brent"], dic["gold"])

    return bot_message


# currency_import()

if __name__ == "__main__":
    print(currency_import())
