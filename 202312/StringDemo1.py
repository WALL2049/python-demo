# �ָ�ÿո�Ĭ�ϣ�/�̶��ַ��ָ��ַ������൱��str��>list��
s = 'alex wusir taibai'
s1 = 'ale:x wus:ir :taibai'
print(len(s))
print(s[1])
s11_1 = s.split()
print(s11_1)    #['alex', 'wusir', 'taibai']
s11_2 = s1.split(':')
print(s11_2)   #['ale', 'x wus', 'ir ', 'taibai']

# �ж��ַ����Ƿ�ȫ�ǿո�
s14_4 = ' n  '
s14_5 = ''
s14_6 = '   '
print(s14_4.isspace())  #False���г��ո���������ַ�
print(s14_5.isspace())  #False����
print(s14_6.isspace())  #True��ȫ�ǿո�


s = '  alexW%Usir  %2%  '
s9_1 = s.strip()
#ɾ���ַ���ǰ��Ŀո�
print(s9_1)

s13_1 = 'С���������ã�����С��'
s13_2 = s13_1.replace('С��','����')
s13_3 = s13_1.replace('С��','����',1)
print(s13_1)
print(s13_2)
print(s13_3)

# s.findͨ��Ԫ�����������ҵ������������Ҳ�������-1
# s.indexͨ��Ԫ�����������ҵ������������Ҳ�������error