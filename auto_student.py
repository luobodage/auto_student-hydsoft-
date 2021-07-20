import re
import time

# import helium as hl
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://eln.hydsoft.net:8081/elms/web/login.jsp')
time.sleep(1)
driver.find_element_by_name('loginId').send_keys('chenxinyu@hydsoft.com')
time.sleep(1)
driver.find_element_by_name('pwd').send_keys('Hydsoft123')
time.sleep(1)
driver.find_element_by_id('btn_login').click()

driver.find_element_by_id('menuChooseCourseNewEntry').click()
time.sleep(3)
html = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
print(html)
detail_url = re.findall(r'<iframe src="(.*?)" id=',html)
print(detail_url)
url = 'http://eln.hydsoft.net:8081/elms/web/' + detail_url[0]
driver.get(url)
time.sleep(30)
for i in range(40):
    time.sleep(3)
    driver.find_element_by_class_name('textLayer').send_keys(Keys.SPACE)
