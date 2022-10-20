# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC # es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.

wd = webdriver.Chrome()
# wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/sample3.html')

# element = wd.find_element(By.CSS_SELECTOR, '[href="http://www.bing.com"]')
element = WebDriverWait(wd, 10, 0.2).until(EC.presence_of_element_located((By.XPATH, '//a[@href="http://www.bing.com"]')))  # 搜索框元素的显式等待 until判断条件。跟进id进行定位，调用EC条件类css 'tag'

element.click()

for handle in wd.window_handles:
    wd.switch_to.window(handle)
    if "必应" in wd.title:
        break


print(wd.title)

element = wd.find_element(By.CSS_SELECTOR, '#sb_form_q')
element.send_keys("俄罗斯\n")

wd.quit()