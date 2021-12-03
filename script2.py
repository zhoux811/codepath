from os import listdir
from os.path import isfile
from os import rename
import re

START = 50
for f_name in listdir():
    if isfile(f_name) and re.match('VoltageData-\d\d\d\d-\d\d-\d\d-\d\d-\d\d-\d\d\.xlsx', f_name):
        print(f_name)
        rename(f_name, str(START) + '.xlsx')
        START += 10
