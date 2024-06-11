import requests
from PIL import Image
import io
from googlemaps import Client

zoom = 13
# Google Maps API 클라이언트 생성 (한달에 $20 까지 무료)
# https://console.cloud.google.com/apis/credentials
Google_API_Key = 'AIzaSyC1cayLwms9aYMJG6-Ezp0G-D-ilMfNBlg'
gmaps = Client(key=Google_API_Key)

# 서울시 지도 생성
seoul_center = gmaps.geocode("서울특별시 중구 을지로2가")[0]['geometry']['location']
seoul_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={seoul_center['lat']},{seoul_center['lng']}&zoom={zoom}&size=400x400&maptype=roadmap"


# 지도 이미지 업데이트 함수
def update_map(mountain):
    global zoom
    gu_map_url = ''
    if mountain['Lat'] and mountain['Lot']:
        lat, lot = float(mountain['Lat']), float(mountain['Lot'])
        gu_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={lat},{lot}&zoom={zoom}&size=400x400&maptype=roadmap"

        marker_url = f"&markers=color:red%7C{lat},{lot}"
        gu_map_url += marker_url

    # 지도 이미지 업데이트
    response = requests.get(gu_map_url + '&key=' + Google_API_Key)
    image = Image.open(io.BytesIO(response.content))
    return image


def zoom_in():
    global zoom
    zoom += 1
    update_map()


def zoom_out():
    global zoom
    if zoom > 1:
        zoom -= 1
    update_map()
