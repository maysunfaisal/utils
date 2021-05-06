import os
import sys
import logging
import requests
from time import sleep

# from bs4 import BeautifulSoup

logging.basicConfig(format="%(asctime)-15s %(name)s %(levelname)s> %(message)s",
                    level=logging.INFO,
                    stream=sys.stdout)
logging.getLogger('comtypes').setLevel(logging.WARN)

URL_COSTCO_NRXC29 = r'https://www.costco.ca/northrock-xc29-73.6-cm-(29-in.)-mountain-bike.product.100674055.html'
URL_COSTCO_NRXC29_2 = r'https://www.costco.ca/northrock-xc29-73.6-cm-(29-in.)-mountain-bike-.product.1465328.html'
URL_COSTCO_NRTanden = r'https://www.costco.ca/northwood-dualdrive-tandem-bicycle.product.100043708.html'

headers = {
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
}


def check_stock(url):
    availabile = False
    response = requests.get(url, timeout=5, headers=headers)
    status_code = response.status_code
    logging.info(status_code)

    if status_code == 200 and 'IN_STOCK' in response.text :
        availabile = True

    return availabile


def notify_mac(message):
    os.system('say ' + message)


def notify_win(message):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()
    engine.stop()


def notify():
    logging.warning("Product is in stock!!!")
    message = "The bike is in stock, place order right now!!"

    for i in range(3):
        if os.name == 'nt':
            notify_win(message)
        else:
            # os.system(f'say, {message}')
            notify_mac(message)

        sleep(5)
        i += 1


if __name__ == "__main__":
    logging.info("Begins")
    url = URL_COSTCO_NRTanden #URL_COSTCO_NRTanden #

    while True:
        # logging.info("Checking inventory")
        if check_stock(url):
            notify()
            # break

        sleep(60)
