"""
task 2
"""
print("write text")
file = open('testlesson.txt', 'w', encoding='utf-8')
s = input()
while s != "":
    file.write(s + "\n")
    s = input()
file.close()
