from django.test import TestCase

# Create your tests here.
# a = '12'
# print(a.split('_')[0])

# a = 10
#
# dict={}
# dict[str(a)] = 'pl'
# print(dict)

# a = '130.0'
# b = '130d'
# # a = float(a)
# # print(a.isdecimal())
# # print(a.isdigit())
# # print(a.isnumeric())
#
# try:
#     a = float(a)
#     b = float(b)
#     print(float(a) == float(b))
# except:
#     print('执行下面的')
#
# print('结束')


a = 130.0
b = '%g'%a
print(b)