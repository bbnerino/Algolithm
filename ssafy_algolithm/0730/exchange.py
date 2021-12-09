import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url)
# 응답 객체의 본문(text)을 해석하여 data 변수에 저장
data = BeautifulSoup(response.text,'html.parser')
print(type(response.text),type(data))
# 해석한 데이터에서 원하는 정보를 선택하고 내용만 kospi에 저장

dollor = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text
yen = data.select_one('#worldExchangeList > li.on > a.head.jpy_usd > div > span.value').text
print(dollor)
print(yen)
