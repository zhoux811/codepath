from pandas import read_excel
from os import listdir
from os.path import isfile

OUPUT_FILE_NAME = 'res.csv'
output = open(OUPUT_FILE_NAME, mode='a')  # Make a new file at the directory where this script is. Write mode: append.
for f_name in listdir():  # scan for all files in current location
    if isfile(f_name) and '.xlsx' in f_name:  # open all .xlsx files in this directory
        print(f_name)
        try:
            df = read_excel(f_name)  # read .xlsx file
            # print(df[df.columns[1]].max() -  df[df.columns[1]].min())  # debug use.
            output.write(
                f_name + '    ' + str(df[df.columns[1]].max() - df[df.columns[1]].min()) + '\n')  # write to output file
        except:
            print('something wrong')

output.close()
