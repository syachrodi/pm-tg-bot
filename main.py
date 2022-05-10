from asyncio.windows_events import NULL
from tkinter import N
from turtle import update
from dotenv import load_dotenv
load_dotenv()


from selenium import webdriver
import os
import requests
from pprint import pprint
from bs4 import BeautifulSoup
import time
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

BASE_URL = 'https://thesphynx.co/swap/32520/'
url = ""
TOKEN = os.getenv('TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
TELEGRAM_API_SEND_MSG = f'https://api.telegram.org/bot{TOKEN}/sendMessage'

items = [
    '32520/0xB361D5953e21Cfde5CD62B89FDf40bc21903A6bb/',
    # '0x71946a5C9dA7C95ee804a9BE561EC15A3F286A7D/'
]

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hi! '+context)

def help(update, context):
    update.message.reply_text('Help!')
    
def price(update, context):
    get_input = update.message.text
    CHAT_ID = update.message.chat.id

    # if(str(CHAT_ID) != "-1001787119421"):
    #     update.message.reply_text('Sorry this bot only work at our group @brc_id\nIf you wanna use this bot, dm our dev @coinranks\nThanks')
    #     pprint(CHAT_ID)
    #     return

    get_input_after = get_input.split('/price ')[1]

    input_after = get_input_after.upper()

    if(input_after == "VEF"):
        url = BASE_URL + "0xd6447d2fa919811c41a064bdbdab1e281f8de9b2"

    elif(input_after == "BPAD"):
        url = BASE_URL + "0x71946a5C9dA7C95ee804a9BE561EC15A3F286A7D"

    elif(input_after == "ELTG"):
        url = BASE_URL + "0xb860eCD8400600c13342a751408737235E177077"

    elif(input_after == "OMNIA"):
        url = BASE_URL + "0x5d4685c2C75581C67b9D6292A065a767bC214681"

    elif(input_after == "EVO"):
        url = BASE_URL + "0x267Ae4bA9CE5ef3c87629812596b0D89EcBD81dD"

    elif(input_after == "SPHYNX"):
        url = BASE_URL + "0x0e11DCE06eF2FeD6f78CEF5144F970E1184b4298"

    elif(input_after == "BTXT"):
        url = BASE_URL + "0x1A8a039007186d7640C1D7Cd7c2606e333D04e03"

    elif(input_after == "PRDS"):
        url = BASE_URL + "0x31226B28add9062c5064a9Bd35eA155F323C6ca6"

    elif(input_after == "YPC"):
        url = BASE_URL + "0x11203a00a9134Db8586381C4B2fca0816476b3FD"

    elif(input_after == "NUMI"):
        url = BASE_URL + "0x6718e47e74497d1564EE76d832309144b83Ef8E8"

    elif(input_after == "MIIDAS"):
        url = BASE_URL + "0x5B534A2Df329195Fd7e5c9AcA1D9ffbdA14A4963"

    elif(input_after == "4MAPS"):
        url = BASE_URL + "0x6D347fdCb302a5879545E01EceE7A176db23dCDa"

    elif(input_after == "YOGO"):
        url = BASE_URL + "0xB361D5953e21Cfde5CD62B89FDf40bc21903A6bb"

    else:
        update.message.reply_text('Token tidak ditemukan!')
        return

    msg = update.message.reply_text("Getting price, please wait...")
    # time.sleep(10)

    driver = webdriver.Chrome(executable_path='C:/path/chromedriver.exe')
    driver.get(url)

    # time.sleep(3)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # pprint(soup.prettify())
    driver.close()
    # liquidity_get = soup.find_all("div", class_="sc-jRQBWg sc-gKclnd gREMsN kxYByf")
    # volume_get = soup.find_all("div", class_="sc-jRQBWg sc-gKclnd gREMsN cdLtbT")

    #   liquidity_get = soup.find_all('div[class="sc-jRQBWg sc-gKclnd gREMsN kxYByf"]')
    # volume_get = soup.find_all('div[class="sc-jRQBWg sc-gKclnd gREMsN cdLtbT"]')

    # pprint(liquidity_get)
    # pprint(volume_get)

    # res = soup.find_next('div', attrs={'class': 'sc-jRQBWg sc-gKclnd gREMsN kxYByf'})
    price = soup.select_one('div[class="sc-gsDKAQ QYecP"]').text
    mcap = soup.select_one('div[class="sc-gsDKAQ zTPCH"]').text
    # liquidity = soup.select('div[class=""]')
    volume = soup.select_one('div[class="sc-gsDKAQ kSMzzt"]').text
    
    # liquidity = liquidity_get.find('div[class="sc-gsDKAQ kSMzzt"]').text
    # volume = volume_get.select_one('div[class="sc-gsDKAQ kSMzzt"]').text

    data = {
        'chat_id': CHAT_ID,
        'text': f'{input_after}\n*Price: {price}*\nMarket cap: [{mcap}]({url})\nLiquidity: Soon\nVolume 24H: {volume}',
        'parse_mode': 'Markdown'
    }
    r = requests.post(TELEGRAM_API_SEND_MSG, data=data)

    context.bot.deleteMessage(message_id = msg.message_id, chat_id = CHAT_ID)
# def echo(update, context):
#     update.message.reply_text(update.message.text)

def error(update, context):
    logger.warning('Update "%s" cause error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("price", price))

    # dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()