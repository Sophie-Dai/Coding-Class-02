# -*- coding: UTF-8 -*-

filename = 'test.txt'
f = open(filename, 'w')

for i in range(10):
    data = 'Row no= %02d Hello World\n' % (i + 1)
    f.write(data)

f.close()
