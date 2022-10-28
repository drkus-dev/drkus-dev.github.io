
# selenium4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

# 이 부분.. 자바를 설치 안 하면 패키징 관련 에러 무지 뜸
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#driver 객체 만들고 url 문자열을 driver.get 함수로 호출
#DRIVER_PATH = 'Users/kys/Documents/GitHub/selenium/chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches",["enable-loggin"])

service_obj = Service(r"/Users/kys/Documents/GitHub/selenium/chromedriver.exe")

DRIVER_PATH = ChromeDriverManager().install()
print(DRIVER_PATH,'<<경로')
#driver = webdriver.Chrome(options=options, service=service_obj)
driver = webdriver.Chrome(DRIVER_PATH)

#n초 딜레이
driver.implicitly_wait(4)
driver.get('https://www.naver.com')
