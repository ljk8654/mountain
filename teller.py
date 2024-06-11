import sys
import time
import telepot
from pprint import pprint
from datetime import date
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

    if res_list:
        for r in res_list:
            noti.sendMessage(user, r)
    else:
        noti.sendMessage(user, f'{name_param}에 해당하는 데이터가 없습니다.')

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
    else:
        noti.sendMessage(chat_id, "모르는 명령어입니다.\n산정보 [산 이름] \n등산로 [산 이름] \n사진 [산 이름] 중 하나의 명령을 입력하세요.")

today = date.today()
print('[', today, ']received token :', noti.TOKEN)

bot = telepot.Bot(noti.TOKEN)
pprint(bot.getMe())

bot.message_loop(handle)
print('Listening...')

while 1:
    time.sleep(10)
