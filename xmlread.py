import requests
import xml.etree.ElementTree as ET
import tkinter
#병원정보 서비스 예제
url = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'

# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key = "VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D"

queryParams = {'serviceKey': service_key, 'pageNo': '1', 'numOfRows': '100','type': 'xml'}

response = requests.get(url, params=queryParams)
print(response.text)
root = ET.fromstring(response.text)


header = ["Name", "Addr", "Lat", "Lot"]
mountain_data = []

row_count = 1
for item in root.iter("item"):
    mountain_dict = {"Name": "", "Location": "", "Height": "", "Description": ""}
    mountain_dict["Name"] = item.findtext("frtrlNm")
    mountain_dict["Location"] = item.findtext("ctpvNm")
    mountain_dict["Height"] = item.findtext("aslAltide")
    mountain_dict["Description"] = item.findtext("addrNm")

    mountain_data.append(mountain_dict)
    yadmNm = item.findtext("frtrlNm")
    addr = item.findtext("ctpvNm")
    Lat = item.findtext("lat")
    Lot = item.findtext("lot")

