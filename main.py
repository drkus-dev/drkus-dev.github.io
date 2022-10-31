# selenium4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

from webdriver_manager.chrome import ChromeDriverManager
DRIVER_PATH = ChromeDriverManager().install()
OPTIONS = webdriver.ChromeOptions()

# 드라이버
driver = webdriver.Chrome(service=Service(DRIVER_PATH),options=OPTIONS)
driver.implicitly_wait(5)

# 프로젝트 관련 코드
# driver.get('http://drkus.dothome.co.kr/')
# imgObj = driver.find_elements(By.CSS_SELECTOR,'div.jumbotron')
# print(imgObj[0].text)

#파이썬 문법
def delay(timeVal):
    time.sleep(timeVal)
    if timeVal < 100 :
        print(timeVal,'보다 작다.')
    return 0
delay(10)

# 슬라이싱
# 0,1,2,3,4
# -5,-4,-3,-2,-1
stdList = ['안','녕','하','세','요']
print(stdList[1:3]) # 녕 하
print(stdList[1:-2]) # 녕 하
print(stdList[1:]) # 녕 하 세 요
print(stdList[:]) # 안 녕 하 세 요
print(stdList[1:100]) # 녕 하 세 요 (stdList[1:]와 동일 문자열 최대 길이만큼 표현0
print(stdList[-1]) # 요
print(stdList[-4]) # 녕
print(stdList[:-3]) # 안 녕
print(stdList[-3:]) # 하 세 요
print(stdList[::1]) # 1은 기본값으로 동일, 안 녕 하 세 요
print(stdList[::-1]) # 뒤집는다. 요 세 하 녕 안






# time.sleep(60)