import requests
import xml.etree.ElementTree as ET
import tkinter
#병원정보 서비스 예제
url = 'http://apis.data.go.kr/B553662/top100FamtListBasiInfoService/getTop100FamtListBasiInfoList'

# 공공데이터포털에서 발급받은 디코딩되지 않은 인증키 입력
service_key = "VFmlOup7ePIpAb7U94%2B7EK7qHRHxNL0iZ%2F4orFG3OqEnNXWkVxtuxswyJYOijCoSa5tvdCyeuxhyujNTsobAdw%3D%3D"

queryParams = {'serviceKey': service_key, 'pageNo': '1', 'numOfRows': '10','type': 'xml'}

response = requests.get(url, params=queryParams)
print(response.text)
root = ET.fromstring(response.text)

window = tkinter.Tk()
window.title("병원정보")

frame = tkinter.Frame(window)
frame.pack()

header = ["Name", "Addr", "Tel", "Url"]

for i, col_name in enumerate(header):
    label = tkinter.Label(frame, text=col_name, font=("Helvetica", 14, "bold"))
    label.grid(row=0, column=i)

row_count = 1
for item in root.iter("item"):
    yadmNm = item.findtext("frtrlNm")
    addr = item.findtext("ctpvNm")
    telno = item.findtext("lat")
    hospUrl = item.findtext("lot")

    data = [yadmNm, addr, telno, hospUrl]
    for i, value in enumerate(data):
        label = tkinter.Label(frame, text=value, font=("Helvetica", 12))
        label.grid(row=row_count, column=i)

    row_count += 1

window.mainloop()