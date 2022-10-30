
# selenium4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time


# 이 부분.. 자바를 설치 안 하면 패키징 관련 에러 무지 뜸
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.common.by import By

#driver 객체 만들고 url 문자열을 driver.get 함수로 호출
#DRIVER_PATH = 'Users/kys/Documents/GitHub/selenium/chromedriver.exe'

OPTIONS = webdriver.ChromeOptions()
# 서비스에 사용될 옵션 추가(안하면 deprecated 에러 무지뜸)

# 드라이버 경로
DRIVER_PATH = ChromeDriverManager().install()
print(DRIVER_PATH,'<<경로')
#driver = webdriver.Chrome(options=options, service=service_obj)


driver = webdriver.Chrome(service=Service(DRIVER_PATH),options=OPTIONS)

#n초 딜레이
# driver.implicitly_wait(20000)
driver.get("https://www.hsd.co.kr/menu/menu_list")
# driver.get('http://drkus.dothome.co.kr/main/')
driver.implicitly_wait(5)
# css seletor으로 class명 찾기 <h4 class="h fz_03"> ... fz_03
# li 태그로 리스트 존재 시, 첫 번째 배열 title 객체의 [0] 값을 가리킨다.
# li 1번째 : 더블함박
# li 2번째 : 해바라기
title = driver.find_elements(By.CSS_SELECTOR,"h4.h.fz_03")
# print(title[i].text)

#반복문 연습, 객체 개수 구하기 len 함수 이용. .count 쓰려다 망했음
print(len(title))
for i in range(len(title)) :
    print(title[i].text)
