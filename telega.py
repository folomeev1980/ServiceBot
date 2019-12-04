import requests

print(requests.get("https://api.telegram.org/bot981624897:AAFD1wu7bBI4XCR3JHvf9iYqRLPZujpDLJM/getMe"))


class Telega():

    def __init__(self, token):
        self.token = token
        self.url = "https://api.telegram.org/bot{}/".format(self.token)

    def get_updates(self, timeout=30):
        method = "getUpdates"
        params = {'timeout': timeout}
        reqr = requests.get(self.url + method, params)
        return reqr.json()["result"]

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

    def chat_id(self):
        chat_id = self.get_last_update()
        return chat_id['message']['chat']['id']

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.url + method, params)
        return resp

#
# t = Telega("981624897:AAFD1wu7bBI4XCR3JHvf9iYqRLPZujpDLJM")
#
# t.send_message(t.chat_id(), "Привет Арсний")
# t.get_updates()
# print(t.chat_id())
