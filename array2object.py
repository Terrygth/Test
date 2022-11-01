import json
import os

path = 'D:\研究生\北京化工\excel2json\json'
files= os.listdir(path)

i = 0
for file in files:
    print(file)
    back = file[len(file) - 4:len(file)]
    print(back)
    if back != 'json':
        continue
    with open(path + '\\' + file, 'r') as f:
        #print(f)
        dict = json.load(f)
    str = json.dumps(dict)
    str = "{\"demo\":" + str + "}"
    dict = json.loads(str)
    #print(str)
    with open(path + '\\' + file, 'w') as f_new:
        json.dump(dict,f_new)

#excel1.save(r'D:\研究生\北京化工\数据\BA111\ACT111.PV_202003010000_202102280000.xlsx')
#excel = openpyxl.load_workbook(r'D:\研究生\北京化工\数据\BA111\ACT111.PV_202003010000_202102280000.xlsx')




