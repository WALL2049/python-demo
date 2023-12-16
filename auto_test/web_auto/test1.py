# coding=utf-8

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.options import Options      # 这个是edge的Options
from selenium.webdriver.support.ui import WebDriverWait # 注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC # es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.

# options = Options()   # 这个一直报错，下面的解决了
options = webdriver.ChromeOptions()

options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--ignore-certificate-errors')
# s = Service(r'C:\Users\123\PycharmProjects\20200302\venv\Scripts\chromedriver.exe')  # webdriver路径
# (service=s,)
wd = webdriver.Chrome(options=options)        #打开浏览器
# wd.implicitly_wait(5)          #隐式等待

wd.get('https://www.baidu.com')    #加载网页
# element = wd.find_element(By.ID, 'kw')                           # css '#id'
# element = wd.find_element(By.NAME, 'wd')
# element = wd.find_element(By.CLASS_NAME, 's_ipt')                # css '.class'
# element = wd.find_element(By.TAG_NAME, 'span')

element = WebDriverWait(wd, 10, 0.2).until(EC.presence_of_element_located((By.XPATH, '//input[@class="s_ipt"]')))  # 搜索框元素的显式等待 until判断条件。跟进id进行定位，调用EC条件类css 'tag'


# element = wd.find_element(By.CSS_SELECTOR, '#kw[class="s_ipt"]')
# element = wd.find_element(By.CSS_SELECTOR, '#layer1 > span')    # 1‘>’表示子元素，2‘ '表示子系元素（后代元素）

# element = wd.find_element(By.CSS_SELECTOR, '[href="......"]')     # 根据属性值，非常常用：'[]'
# element = wd.find_element(By.CSS_SELECTOR, '#layer1[href="......"]')     # 表示两个条件同时满足
# element = wd.find_element(By.CSS_SELECTOR, '#layer1[href*="baidu"]')     # 包含baidu
# element = wd.find_element(By.CSS_SELECTOR, '#layer1[href^="https"]')     # 以https开头
# element = wd.find_element(By.CSS_SELECTOR, '#layer1[href$="gov.cn"]')     # 以gov.cn结尾



# elements = wd.find_elements(By.CSS_SELECTOR, '')
# for element in elements:
#     pass

# 直接enter
# element.send_keys('python\n')


# 使用click
element.send_keys('python')
element = wd.find_element(By.ID, 'su')
print(element.get_attribute('value'))
print('----------------------------')
print(element.get_attribute('outerHTML'))
print('----------------------------')
print(element.get_attribute('innerHTML'))
element.click()
print(dir(webdriver))

# open_browser(txt)

wd.quit()

# while True:
#     try:
#         pass
#         break
#     except:
#         time.sleep(1)