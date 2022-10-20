# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC # es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.

wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample2.html')
# wd.switch_to.frame('frame1')      # id或者name都行
wd.switch_to.frame(wd.find_element(By.CSS_SELECTOR, 'iframe[src="sample1.html"]'))       # 别的元素也可以
elements = wd.find_elements(By.CSS_SELECTOR, '.plant')

print(wd.title)

for element in elements:
    print(element.get_attribute('innerHTML'))
    print(element.get_attribute('outerHTML'))
    print('-------------------------------')

wd.switch_to.default_content()
wd.find_element(By.CSS_SELECTOR, '#outerbutton').click()

wd.quit()
