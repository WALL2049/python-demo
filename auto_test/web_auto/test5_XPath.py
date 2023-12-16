# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # 注意区分大小写，导入WebDriverWait等待的类
from selenium.webdriver.support import expected_conditions as EC # es,expected_conditions首字母，方便调用方法。as取一个别名，调方法的话直接EC.

wd = webdriver.Chrome()
# wd.implicitly_wait(5)

wd.get('https://cdn2.byhy.net/files/selenium/test1.html')

element = wd.find_element(By.XPATH, "/html/body/div")  # 绝对路径
element = wd.find_element(By.XPATH, "//div//p")    # 相对路径
element = wd.find_element(By.XPATH, "//div/*")      # 通配符


# 根据属性来说，和CSS区别在于，CSS只要选择部分元素就行，比如：'p[.capital]',而XPath需要全选，复制粘贴即可
# element = wd.find_element(By.XPATH, "//p[@class="capital huge-city"]")     # 根据属性
# 当某个属性不足以唯一区别某一个元素时，也可以采取多个条件组合的方式，如下：
xpath= "//input[@type='XX' and @name='XX']"


element = wd.find_element(By.XPATH, "//*[@multiple]")      # 具有multiple属性的所有页面元素
element = wd.find_element(By.XPATH, "//*[contains(@style,'color')]")      # style属性值 包含 color 字符串的 页面元素
element = wd.find_element(By.XPATH, "//*[starts-with(@style,'color')]")      # style属性值 以 color 字符串 开头 的 页面元素
element = wd.find_element(By.XPATH, "//*[ends-with(@style,'color')]")      # 以’‘结尾，但是它是xpath2.0,目前不支持

element = wd.find_element(By.XPATH, "//p[2]")      # 选取p类型第2个的子元素
element = wd.find_element(By.XPATH, "//div/p[2]")      # 选取父元素为div 中的 p类型 第2个 子元素
element = wd.find_element(By.XPATH, "//div/*[2]")      # 选取父元素为div的第2个子元素，不管是什么类型
element = wd.find_element(By.XPATH, "//p[last()]")      # 选取p类型倒数第1个子元素
element = wd.find_element(By.XPATH, "//p[last()-1]")      # 选取p类型倒数第2个子元素
element = wd.find_element(By.XPATH, "//div/p[last()-2]")      # 选取p类型倒数第2个子元素
element = wd.find_element(By.XPATH, "//option[position()<=2]")      # 选取option类型第1到2个子元素
element = wd.find_element(By.XPATH, "//option[position()<3]")     # 或者这个

element = wd.find_element(By.XPATH, "//*[@class='multi_choice']/*[position()<=3]")      # 选择class属性为multi_choice的前3个子元素
element = wd.find_element(By.XPATH, "//*[@class='multi_choice']/*[position()>=last()-2]")      # 选择class属性为multi_choice的后3个子元素
element = wd.find_element(By.XPATH, "//option | //h4")      #选所有的option元素 和所有的 h4 元素, //*[@class='single_choice'] | //*[@class='multi_choice']
element = wd.find_element(By.CSS_SELECTOR, "option, h4")      # 等同于CSS

element = wd.find_element(By.XPATH, "//*[@id='china']/.. ")      #父节点
element = wd.find_element(By.XPATH, " //*[@id='china']/../../..")      #一直往上
element = wd.find_element(By.XPATH, "//*[@class='single_choice']/following-sibling::*")      #后面的所有兄弟节点
element = wd.find_element(By.CSS_SELECTOR, ".single_choice ~ *")      #等同于CSS

element = wd.find_element(By.XPATH, "//*[@class='single_choice']/preceding-sibling::*")      #前面的 兄弟节点
