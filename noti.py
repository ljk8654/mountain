import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.parse import urlencode, quote_plus
import traceback

SERVICE_KEY = 'VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D'
TOKEN = '7480898950:AAGNIQEJq4Ysh3dp-NFsdmtcRWSwow-rSVg'
MAX_MSG_LENGTH = 300
BASE_URL = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'
MOUNTAIN_INFO_URL = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoOpenAPI2'
TRAIL_INFO_URL = 'http://api.forest.go.kr/openapi/service/cultureInfoService/gdTrailInfoOpenAPI'
MOUNTAIN_PICTURE_URL = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoImgOpenAPI2'

QUERY_PARAMS = {'serviceKey': SERVICE_KEY, 'pageNo': '1', 'numOfRows': '100', 'type': 'xml'}
MOUNTAIN_INFO_PARAMS = {'serviceKey': SERVICE_KEY, 'searchWrd': '', 'pageNo': '1', 'numOfRows': '10'}
TRAIL_INFO_PARAMS = {'serviceKey': SERVICE_KEY, 'searchMtNm': '', 'pageNo': '1', 'numOfRows': '10'}
MOUNTAIN_PICTURE_PARAMS = {'serviceKey': SERVICE_KEY, 'mntiListNo': '', 'pageNo': '1', 'numOfRows': '1'}

bot = telepot.Bot(TOKEN)

def getMountainInfo(name_param):
    res_list = []
    MOUNTAIN_INFO_PARAMS['searchWrd'] = name_param
    query_string = urlencode(MOUNTAIN_INFO_PARAMS, quote_via=quote_plus)
    url = MOUNTAIN_INFO_URL + '?' + query_string
    print(f"Encoded URL: {url}")  # 디버깅을 위해 URL 출력
    try:
        res_body = urlopen(url).read()
        soup = BeautifulSoup(res_body, 'lxml-xml')  # XML 파서 사용
        print(f"Response: {soup.prettify()}")  # 전체 응답을 출력하여 확인
        items = soup.findAll('item')
        for item in items:
            info = {
                '산이름': item.find('mntiname').get_text(strip=True) if item.find('mntiname') else 'N/A',
                '높이': item.find('mntiheight').get_text(strip=True) if item.find('mntiheight') else 'N/A',
                '위치': item.find('mntiadmin').get_text(strip=True) if item.find('mntiadmin') else 'N/A',
                '특징': item.find('mntidetails').get_text(strip=True) if item.find('mntidetails') else 'N/A'
            }
            row = f"산 이름: {info['산이름']}, 높이: {info['높이']}m, 위치: {info['위치']}, 특징: {info['특징']}"
            res_list.append(row)
    except Exception as e:
        print(f"Error: {e}")
    return res_list

def getTrailInfo(name_param):
    res_list = []
    TRAIL_INFO_PARAMS['searchMtNm'] = name_param
    query_string = urlencode(TRAIL_INFO_PARAMS, quote_via=quote_plus)
    url = TRAIL_INFO_URL + '?' + query_string
    print(f"Encoded URL: {url}")  # 디버깅을 위해 URL 출력
    try:
        res_body = urlopen(url).read()
        soup = BeautifulSoup(res_body, 'lxml-xml')  # XML 파서 사용
        print(f"Response: {soup.prettify()}")  # 전체 응답을 출력하여 확인
        items = soup.findAll('item')
        for item in items:
            info = {
                '등산로이름': item.find('mntiname').get_text(strip=True) if item.find('mntiname') else 'N/A',
                '등산로길이': item.find('mtlength').get_text(strip=True) if item.find('mtlength') else 'N/A',
                '등산로소요시간': item.find('usetime').get_text(strip=True) if item.find('usetime') else 'N/A'
            }
            row = f"등산로 이름: {info['등산로이름']}, 길이: {info['등산로길이']}km, 소요 시간: {info['등산로소요시간']}"
            res_list.append(row)
    except Exception as e:
        print(f"Error: {e}")
    return res_list

def getMountainPicture(name_param):
    res_list = []
    MOUNTAIN_PICTURE_PARAMS['mntiListNo'] = name_param
    query_string = urlencode(MOUNTAIN_PICTURE_PARAMS, quote_via=quote_plus)
    url = MOUNTAIN_PICTURE_URL + '?' + query_string
    print(f"Encoded URL: {url}")  # 디버깅을 위해 URL 출력
    try:
        res_body = urlopen(url).read()
        soup = BeautifulSoup(res_body, 'lxml-xml')  # XML 파서 사용
        print(f"Response: {soup.prettify()}")  # 전체 응답을 출력하여 확인
        items = soup.findAll('item')
        for item in items:
            info = {
                '이미지URL': item.find('imgurl').get_text(strip=True) if item.find('imgurl') else 'N/A'
            }
            row = f"이미지 URL: {info['이미지URL']}"
            res_list.append(row)
    except Exception as e:
        print(f"Error: {e}")
    return res_list

def sendMessage(user, msg):
    try:
        if msg.strip():  # 메시지가 비어 있는지 확인
            bot.sendMessage(user, msg)
        else:
            bot.sendMessage(user, "요청한 정보가 없습니다.")
    except:
        traceback.print_exc(file=sys.stdout)