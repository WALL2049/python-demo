
with open('test.txt', 'w') as file:
    file.write('123'+'\n'+'456')

# ָ�����⣬ͬһ�δ�������д��������
with open('test.txt', 'r') as file:
    result = file.read()
    print(result)


# result = '-'.join(('a', 'b', 'c'))
# print(result)



