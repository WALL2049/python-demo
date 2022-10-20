# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By


wd = webdriver.Chrome()
wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample1a.html')
# elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-child(2)')
# elements = wd.find_elements(By.CSS_SELECTOR, 'p:nth-last-child(1)')
elements = wd.find_elements(By.CSS_SELECTOR, 'span:nth-of-type(1)')
# elements = wd.find_elements(By.CSS_SELECTOR, '#t1 p:nth-child(odd)')     # 奇数或者偶数
# elements = wd.find_elements(By.CSS_SELECTOR, '#t1 h3 + span ')     # 兄弟元素，紧跟的元素
# elements = wd.find_elements(By.CSS_SELECTOR, '#t1 h3 ~ span ')     # 兄弟元素，后面的元素

for element in elements:
    print(element.get_attribute('outerHTML'))
    print(element.get_attribute('innerHTML'))
    print('----------------------------')

wd.quit()