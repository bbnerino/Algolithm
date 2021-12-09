import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/"
response = requests.get(url)
# 응답 객체의 본문(text)을 해석하여 data 변수에 저장
data = BeautifulSoup(response.text,'html.parser')
print(type(response.text),type(data))
# 해석한 데이터에서 원하는 정보를 선택하고 내용만 kospi에 저장

kospi = data.select_one('#KOSPI_now').text
# <span class="num num2" id="KOSPI_now">3,224.69</span> -> .text => 3224.69 
print(kospi)