import requests
import xml.etree.ElementTree as ET
from urllib.parse import urlencode, unquote
import telepot
import traceback

SERVICE_KEY = "VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D"
SERVICE_KEY = unquote(SERVICE_KEY)
TOKEN = '7480898950:AAGNIQEJq4Ysh3dp-NFsdmtcRWSwow-rSVg'
MAX_MSG_LENGTH = 300

MOUNTAIN_INFO_URL = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoOpenAPI2'
TRAIL_INFO_URL = 'http://api.forest.go.kr/openapi/service/cultureInfoService/gdTrailInfoOpenAPI'
MOUNTAIN_PICTURE_URL = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoImgOpenAPI2'
POI_URL = 'http://apis.data.go.kr/B553662/sghtngPoiInfoService/getSghtngPoiInfoList'

MOUNTAIN_INFO_PARAMS = {'serviceKey': SERVICE_KEY, 'searchWrd': '', 'pageNo': '1', 'numOfRows': '10'}
TRAIL_INFO_PARAMS = {'serviceKey': SERVICE_KEY, 'searchMtNm': '', 'pageNo': '1', 'numOfRows': '10'}
MOUNTAIN_PICTURE_PARAMS = {'serviceKey': SERVICE_KEY, 'mntiListNo': '', 'pageNo': '1', 'numOfRows': '1'}
POI_PARAMS = {'serviceKey': SERVICE_KEY, 'srchFrtrlNm': '', 'pageNo': '1', 'numOfRows': '100', 'type': 'xml'}

bot = telepot.Bot(TOKEN)

def getMountainInfo(name_param):
    res_list = []
    MOUNTAIN_INFO_PARAMS['searchWrd'] = name_param
    response = requests.get(MOUNTAIN_INFO_URL, params=MOUNTAIN_INFO_PARAMS)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    for item in root.iter("item"):
        mountain_name = item.findtext("mntiname", default="N/A")
        height = item.findtext("mntihigh", default="N/A")  # 'mntiheight'가 아닌 'mntihigh'
        location = item.findtext("mntiadd", default="N/A")  # 'mntiadmin'이 아닌 'mntiadd'
        description = item.findtext("mntidetails", default="N/A")
        res_list.append(f"산 이름: {mountain_name}, 높이: {height}m, 위치: {location}, 특징: {description}")
    return res_list

def getTrailInfo(name_param):
    res_list = []
    TRAIL_INFO_PARAMS['searchMtNm'] = name_param
    response = requests.get(TRAIL_INFO_URL, params=TRAIL_INFO_PARAMS)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    for item in root.iter("item"):
        trail_name = item.findtext("mntnm", default="N/A")  # 'mntiname'이 아닌 'mntnm'
        trail_length = item.findtext("mntheight", default="N/A")  # 'mtlength'가 아닌 'mntheight'
        trail_time = item.findtext("etccourse", default="N/A")  # 'usetime'이 아닌 'etccourse'
        res_list.append(f"등산로 이름: {trail_name}, 높이: {trail_length}m, 등산로 코스: {trail_time}")
    return res_list

def getMountainPicture(name_param):
    res_list = []
    MOUNTAIN_INFO_PARAMS['searchWrd'] = name_param
    response = requests.get(MOUNTAIN_INFO_URL, params=MOUNTAIN_INFO_PARAMS)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    mountain_list_no = None

    for item in root.iter("item"):
        mountain_list_no = item.findtext('mntilistno')
        break

    if not mountain_list_no:
        return ["해당 산의 사진 정보를 찾을 수 없습니다."]

    MOUNTAIN_PICTURE_PARAMS['mntiListNo'] = mountain_list_no
    response = requests.get(MOUNTAIN_PICTURE_URL, params=MOUNTAIN_PICTURE_PARAMS)
    response.raise_for_status()
    root = ET.fromstring(response.content)

    for item in root.iter("item"):
        image_url = 'http://www.forest.go.kr/images/data/down/mountain/' + item.findtext('imgfilename', default='N/A')
        res_list.append(f"이미지 URL: {image_url}")
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)
