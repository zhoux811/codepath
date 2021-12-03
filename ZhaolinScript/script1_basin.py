from os import listdir, rename, mkdir
from os.path import isfile
from shutil import copyfile
from pandas import read_excel
import re, csv, time

START = 40
STEP = 10


def get_that_n(xlsx_f):
    df = read_excel(xlsx_f)  # read .xlsx file
    # print(df[df.columns[1]].max() -  df[df.columns[1]].min())  # debug use.
    return str(df[df.columns[1]].max() - df[df.columns[1]].min())


file_list = [f for f in listdir() if (isfile(f) and re.match('VoltageData-\d\d\d\d-\d\d-\d\d-\d\d-\d\d-\d\d\.xlsx', f))]
L = len(file_list)
MID_IDX = L // 2 if L % 2 == 0 else L // 2 + 1

with open('log_script1_basin.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['target file name', 'value', 'original filename', 'execute time log'])

    for f_name in file_list[:MID_IDX]:
        START += STEP
        copyfile(f_name, '-' + str(START) + '.xlsx')
        writer.writerow(['-' + str(START), get_that_n(f_name), f_name, time.asctime(time.localtime(time.time()))])

    START = START - STEP if L % 2 == 1 else START

    for f_name in file_list[MID_IDX:]:
        copyfile(f_name, '-' + str(START) + 'r.xlsx')
        writer.writerow(['-' + str(START) + 'r', get_that_n(f_name), f_name, time.asctime(time.localtime(time.time()))])
        START -= STEP
