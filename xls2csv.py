import pandas as pd
import sys
import os

arg = sys.argv[1]
if(os.path.isdir(arg)):
    os.chdir(arg)
    file_names = os.listdir(arg)
elif(os.path.isfile(arg)):
    file_names = [arg]
else:
    raise ValueError('Illegal Argument: {} must be a directory or a file'.format(arg))

for file_name in file_names:
    if(file_name.find('xls') != -1):
        df = pd.read_excel(file_name)
        df.to_csv(file_name.replace('xls', 'csv'), encoding='utf-8')
