import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti

def replyMountainData(name_param, user, type_param='info'):
    if type_param == 'info':
        res_list = noti.getMountainInfo(name_param)
    elif type_param == 'trail':
        res_list = noti.getTrailInfo(name_param)
    elif type_param == 'picture':
        res_list = noti.getMountainPicture(name_param)
    else:
        noti.sendMessage(user, '알 수 없는 타입입니다.')
        return

    msg = ''
    for r in res_list:
        if len(r + msg) + 1 > noti.MAX_MSG_LENGTH:
            noti.sendMessage(user, msg)
            msg = r + '\n'
        else:
            msg += r + '\n'
    if msg:
        noti.sendMessage(user, msg)
    else:
        noti.sendMessage(user, f'{name_param}에 해당하는 데이터가 없습니다.')

def save(user, name_param):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, mountain TEXT, PRIMARY KEY(user, mountain))')
    try:
        cursor.execute('INSERT INTO users(user, mountain) VALUES (?, ?)', (user, name_param))
    except sqlite3.IntegrityError:
        noti.sendMessage(user, '이미 해당 정보가 저장되어 있습니다.')
        return
    else:
        noti.sendMessage(user, '저장되었습니다.')
        conn.commit()

def check(user):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users(user TEXT, mountain TEXT, PRIMARY KEY(user, mountain))')
    cursor.execute('SELECT * from users WHERE user=?', (user,))
    for data in cursor.fetchall():
        row = 'id:' + str(data[0]) + ', mountain:' + data[1]
        noti.sendMessage(user, row)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')

    if text.startswith('산정보') and len(args) > 1:
        replyMountainData(args[1], chat_id, 'info')
    elif text.startswith('등산로') and len(args) > 1:
        replyMountainData(args[1], chat_id, 'trail')
    elif text.startswith('사진') and len(args) > 1:
        replyMountainData(args[1], chat_id, 'picture')
    elif text.startswith('저장') and len(args) > 1:
        save(chat_id, args[1])
    elif text.startswith('확인'):
        check(chat_id)
    else:
        noti.sendMessage(chat_id, "모르는 명령어입니다.\n산정보 [산 이름] \n등산로 [산 이름] \n사진 [산 이름] \n저장 [산 이름] \n확인 중 하나의 명령을 입력하세요.")

today = date.today()
print('[', today, ']received token :', noti.TOKEN)

bot = telepot.Bot(noti.TOKEN)
pprint(bot.getMe())

bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)
