# 分割：用空格（默认）/固定字符分割字符串（相当于str—>list）
s = 'alex wusir taibai'
s1 = 'ale:x wus:ir :taibai'
print(len(s))
print(s[1])
s11_1 = s.split()
print(s11_1)    #['alex', 'wusir', 'taibai']
s11_2 = s1.split(':')
print(s11_2)   #['ale', 'x wus', 'ir ', 'taibai']

# 判断字符串是否全是空格
s14_4 = ' n  '
s14_5 = ''
s14_6 = '   '
print(s14_4.isspace())  #False：有除空格外的其他字符
print(s14_5.isspace())  #False：空
print(s14_6.isspace())  #True：全是空格


s = '  alexW%Usir  %2%  '
s9_1 = s.strip()
#删除字符串前后的空格
print(s9_1)

s13_1 = '小明，哈喽你好，我是小明'
s13_2 = s13_1.replace('小明','张三')
s13_3 = s13_1.replace('小明','张三',1)
print(s13_1)
print(s13_2)
print(s13_3)

# s.find通过元素找索引，找到返回索引，找不到返回-1
# s.index通过元素找索引，找到返回索引，找不到返回error