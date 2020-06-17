#
# s = input('write some txt ')
# a = [s.find('h') + 1]
# b = [s.rfind('h') - 1]
# c = (a + b).replace("h", "H")
# d = a + b + c
# print(d)
s = input('write some text')
a = s[:s.find('h') + 1]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
d = a + b.replace('h', 'H') + c
print(d)
