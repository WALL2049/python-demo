# dic = {'c':1, 'b':4, 'a':3, 'd':2}
#
# k = list(dic.keys())
# v = list(dic.values())
# k.sort()
# v.sort()
# print(k)
# print(v)
# dic2 = {}
# for i in range(4):
# 	dic2[k[i]] = v[i]
#
# print(dic2)

# a = lambda x,y:x+y
# b = a(1,2)
# print(b)

# a = list(map(lambda x:x**2, [0,1,2,3,4]))
# print(a)
#
# b = list(filter(lambda x:x>2, [0,1,2,3,4]))
# print(b)

def testRaise1():
	for i in range(5):
		if i == 2:
			raise NameError
		print(i)
	print('end...')

def testRaise2():
	for i in range(5):
		try:
			if i==2:
				raise NameError
		except NameError:
			print('raise a NameError!')
		print(i)
	print('end...')

testRaise2()
testRaise1()
