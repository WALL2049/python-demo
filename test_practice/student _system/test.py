
with open('test.txt', 'w') as file:
    file.write('123'+'\n'+'456')

# 指针问题，同一次打开连续读写会有问题
with open('test.txt', 'r') as file:
    result = file.read()
    print(result)


# result = '-'.join(('a', 'b', 'c'))
# print(result)



