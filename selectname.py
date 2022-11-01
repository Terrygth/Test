import openpyxl,string
import os

path = 'D:\研究生\北京化工\数据\BA111'
files= os.listdir(path)
with open('D:\myapp\public\select_name.txt','w') as f:
    for file in files:
        print(file)
        back = file[len(file) - 4:len(file)]
        print(back)
        if back == '.csv':
            continue
        title = file[0:len(file) - 5]
        f.write(title+',\n')

f.close()





