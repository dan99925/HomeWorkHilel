s = input('write some text')
a = s[s.find('h')]
b = s[s.find('h') + 1:s.rfind('h')]
c = s[s.rfind('h'):]
d = a + b.replace('h', 'H') + c
print(d)
