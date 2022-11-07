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
driver.get('http://drkus-dev.github.io')
# imgObj = driver.find_elements(By.CSS_SELECTOR,'div.jumbotron')
# print(imgObj[0].text)

#경고 창 다루기
# from selenium.webdriver.common.alert import Alert

driver.implicitly_wait(10)
# driver.switch_to.alert.dismiss()
driver.switch_to.alert.accept()

# ctr+클릭하여 새 창 열고 이동
from selenium.webdriver.common.keys import Keys
target = driver.find_elements(By.CSS_SELECTOR,'#a-link')  # 클릭하고 싶은 것 선택
target.send_keys(Keys.CONTROL +"\n")




# Alert(driver).dismiss()
# dd = Alert(driver).getText()









