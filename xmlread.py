from io import BytesIO
from PIL import Image, ImageTk
import requests
import xml.etree.ElementTree as ET
from urllib.parse import unquote

# 상수 정의
BASE_URL = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'
MOUNTAIN_INFO_URL = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoOpenAPI2'
TRAIL_INFO_URL = 'http://api.forest.go.kr/openapi/service/cultureInfoService/gdTrailInfoOpenAPI'
MOUNTAIN_PICTURE_URL = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoImgOpenAPI2'

# API 키 (디코딩됨)
SERVICE_KEY = "VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D"
SERVICE_KEY = unquote(SERVICE_KEY)

# API 파라미터
QUERY_PARAMS = {'serviceKey': SERVICE_KEY, 'pageNo': '1', 'numOfRows': '100', 'type': 'xml'}
MOUNTAIN_INFO_PARAMS = {'serviceKey': SERVICE_KEY, 'searchWrd': '', 'pageNo': '1', 'numOfRows': '10'}
TRAIL_INFO_PARAMS = {'serviceKey': SERVICE_KEY, 'searchMtNm': '', 'pageNo': '1', 'numOfRows': '10'}
MOUNTAIN_PICTURE_PARAMS = {'serviceKey': SERVICE_KEY, 'mntiListNo': '', 'pageNo': '1', 'numOfRows': '1'}


def fetch_mountain_data():
    # API 요청
    response = requests.get(BASE_URL, params=QUERY_PARAMS)
    response.raise_for_status()  # HTTP 응답 코드 확인
    root = ET.fromstring(response.text)

    mountain_data = []
    for item in root.iter("item"):
        mountain_dict = {
            "Name": item.findtext("frtrlNm"),
            "Location": item.findtext("ctpvNm"),
            "Height": item.findtext("aslAltide"),
            "Description": item.findtext("addrNm"),
            "Lat": float(item.findtext("lat") or 0),
            "Lot": float(item.findtext("lot") or 0)
        }
        mountain_data.append(mountain_dict)

    return mountain_data


def fetch_mountain_information(mountain_name):
    # 산 정보 API 요청
    MOUNTAIN_INFO_PARAMS['searchWrd'] = mountain_name
    mountain_info_response = requests.get(MOUNTAIN_INFO_URL, params=MOUNTAIN_INFO_PARAMS)
    mountain_info_response.raise_for_status()

    mountain_info_root = ET.fromstring(mountain_info_response.text)
    for item in mountain_info_root.iter("item"):
        MOUNTAIN_PICTURE_PARAMS['mntiListNo'] = item.findtext('mntilistno')
        return item.findtext('mntidetails')

    return "정보 없음"


def fetch_mountain_picture(mountain_name):
    # 산 사진 API 요청
    MOUNTAIN_INFO_PARAMS['searchWrd'] = mountain_name
    mountain_info_response = requests.get(MOUNTAIN_INFO_URL, params=MOUNTAIN_INFO_PARAMS)
    mountain_info_response.raise_for_status()

    mountain_info_root = ET.fromstring(mountain_info_response.text)
    mountain_list_no = None

    for item in mountain_info_root.iter("item"):
        mountain_list_no = item.findtext('mntilistno')
        break

    if not mountain_list_no:
        return None

    MOUNTAIN_PICTURE_PARAMS['mntiListNo'] = mountain_list_no
    mountain_picture_response = requests.get(MOUNTAIN_PICTURE_URL, params=MOUNTAIN_PICTURE_PARAMS)
    mountain_picture_response.raise_for_status()

    mountain_picture_root = ET.fromstring(mountain_picture_response.text)
    for item in mountain_picture_root.iter("item"):
        image_url = 'http://www.forest.go.kr/images/data/down/mountain/' + item.findtext('imgfilename')
        icon_response = requests.get(image_url)
        icon_response.raise_for_status()

        icon_image = Image.open(BytesIO(icon_response.content))
        return icon_image

    return None

def fetch_trail_information(mountain_name):
    # 등산로 정보 API 요청
    print(mountain_name)
    TRAIL_INFO_PARAMS['searchMtNm'] = mountain_name
    trail_info_response = requests.get(TRAIL_INFO_URL, params=TRAIL_INFO_PARAMS)
    trail_info_response.raise_for_status()

    trail_info_root = ET.fromstring(trail_info_response.text)
    for item in trail_info_root.iter("item"):
        return item.findtext('etccourse'),item.findtext('details')  # 등산로와 정보

    return "정보 없음"