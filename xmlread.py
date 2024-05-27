import requests
import xml.etree.ElementTree as ET
import tkinter
from urllib.parse import unquote
#병원정보 서비스 예제

mountain_info = ''
url = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'
moutain_info_url = 'http://apis.data.go.kr/1400000/service/cultureInfoService2/mntInfoOpenAPI2'

# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key = "VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D"
service_key = unquote(service_key)
queryParams = {'serviceKey': service_key, 'pageNo': '1', 'numOfRows': '100','type': 'xml'}
moutain_info_params = {'serviceKey': service_key, 'searchWrd':'','pageNo': '1', 'numOfRows': '10'}

response = requests.get(url, params=queryParams)

print(response.text)
root = ET.fromstring(response.text)

header = ["Name", "Addr", "Lat", "Lot"]
mountain_data = []

for item in root.iter("item"):
    mountain_dict = {"Name": "", "Location": "", "Height": "", "Description": ""}
    mountain_dict["Name"] = item.findtext("frtrlNm")
    mountain_dict["Location"] = item.findtext("ctpvNm")
    mountain_dict["Height"] = item.findtext("aslAltide")
    mountain_dict["Description"] = item.findtext("addrNm")

    mountain_data.append(mountain_dict)

def mountain_information(mountain_n):
    moutain_info_params['searchWrd'] = mountain_n
    moutain_info_response = requests.get(moutain_info_url, params=moutain_info_params)
    moutain_info_root = ET.fromstring(moutain_info_response.text)

    for item in moutain_info_root.iter("item"):
        return item.findtext('mntidetails')
