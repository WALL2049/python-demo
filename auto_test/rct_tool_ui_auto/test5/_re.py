import re

testtxt = r'124\ntestrct123dq6721eh90nuiohtestrct123awdgh21445tnk'

# result = re.match(r'124\\n', testtxt)
# print(dir(result))
# print(result.start())
# print(result.group())

# result = re.search(r'124\\n', testtxt)
# print(dir(result))
# print(result.start())
# print(result.group())

# result = re.findall('testrct123', testtxt)
# print(dir(result))
# print(result)

p = re.compile('testrct123')
p.search(testtxt)
print(dir(p))


