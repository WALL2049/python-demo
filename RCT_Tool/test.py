# coding=utf-8


import re
import os
import PySimpleGUI as sg
import sys
import paramiko
import time
from selenium import webdriver # 导入webdrive这个类
from selenium.webdriver.support.ui import WebDriverWait # 注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC # es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.
from selenium.webdriver.common.by import By # 通过by进行元素定位
from selenium.webdriver.chrome.options import Options

from selenium import webdriver  # 导入selenium模块
#
#
# b = webdriver.Chrome()  # 打开浏览器
# b.get('https://www.baidu.com/')
# # b.get('https://www.zhibo8.cc/')  # 打开一个页面
#
# print(b.title)  # 判断访问元素的title
# print(b.current_url)  # 查看当期的url/

os.system('route print\n')

#
# clear()  # 清除对象内容
# submit()  # 如果有submit按钮，自动提交表单
# text  # 获取文本信息
# get_attribute()  # 获取属性值
#
# b.back  # 返回
#
#
#
# find_element_by_name()  # 根据name属性定位
#
# find_element_by_class_name()  # 根据class属性定位
#
# find_element_by_link_text()  # 根据文字链接
#
# find_element_by_partial_link_text()  # 根据文字链接的一部分(模糊查询)
#
# find_element_by_tag_name()  # 根据标签名称
#
# find_element_by_css_selector()  # 根据css选择器定位  在火狐浏览,可以用firebug直接采集
#
#
#
#
# b.find_element('//*[@id="m_adv"]')   # 根据xpath定位


