# -*- coding: UTF-8 -*-

filename = 'test.txt'
f = open(filename, 'a')

for i in range(5):
    append_data = '\nPlease append this row.'
    f.write(append_data)

f.close()
