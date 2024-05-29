from io import BytesIO
from PIL import Image, ImageTk
import requests
import xml.etree.ElementTree as ET
from urllib.parse import unquote

url = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'
mountain_info_url = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoOpenAPI2'
mountain_picture_url = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoImgOpenAPI2'
# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key = "VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D"
service_key = unquote(service_key)
query_params = {'serviceKey': service_key, 'pageNo': '1', 'numOfRows': '100', 'type': 'xml'}
mountain_info_params = {'serviceKey': service_key, 'searchWrd': '', 'pageNo': '1', 'numOfRows': '10'}
mountain_picture_params = {'serviceKey': service_key, 'mntiListNo': '', 'pageNo': '1', 'numOfRows': '1'}

response = requests.get(url, params=query_params)
response.raise_for_status()  # HTTP 응답 코드 확인

root = ET.fromstring(response.text)

header = ["Name", "Addr", "Lat", "Lot"]
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


def mountain_information(mountain_name):
    mountain_info_params['searchWrd'] = mountain_name
    mountain_info_response = requests.get(mountain_info_url, params=mountain_info_params)
    mountain_info_response.raise_for_status()

    mountain_info_root = ET.fromstring(mountain_info_response.text)

    for item in mountain_info_root.iter("item"):
        mountain_picture_params['mntiListNo'] = item.findtext('mntilistno')
        return item.findtext('mntidetails')

    return "No information available"


def mountain_picture(mountain_name):
    mountain_info_params['searchWrd'] = mountain_name
    mountain_info_response = requests.get(mountain_info_url, params=mountain_info_params)
    mountain_info_response.raise_for_status()

    mountain_info_root = ET.fromstring(mountain_info_response.text)
    mountain_list_no = None

    for item in mountain_info_root.iter("item"):
        mountain_list_no = item.findtext('mntilistno')
        break

    if not mountain_list_no:
        return None

    mountain_picture_params['mntiListNo'] = mountain_list_no
    mountain_picture_response = requests.get(mountain_picture_url, params=mountain_picture_params)
    mountain_picture_response.raise_for_status()

    mountain_picture_root = ET.fromstring(mountain_picture_response.text)

    for item in mountain_picture_root.iter("item"):
        image_url = 'http://www.forest.go.kr/images/data/down/mountain/' + item.findtext('imgfilename')
        icon_response = requests.get(image_url)
        icon_response.raise_for_status()

        icon_image = Image.open(BytesIO(icon_response.content))
        return icon_image

    return None
