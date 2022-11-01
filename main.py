import openpyxl,string
import os

path = 'D:\研究生\北京化工\数据\BA111'
files= os.listdir(path)

i = 0
for file in files:
    print(file)
    excel = openpyxl.Workbook()
    back = file[len(file) - 4:len(file)]
    print(back)
    if back == '.csv':
        continue
    f = open(path + '\\' + file,'r+')
    sheet = excel.active
    sheet.title = file[0:len(file)-5]
#excel1.save(r'D:\研究生\北京化工\数据\BA111\ACT111.PV_202003010000_202102280000.xlsx')
#excel = openpyxl.load_workbook(r'D:\研究生\北京化工\数据\BA111\ACT111.PV_202003010000_202102280000.xlsx')
    sheets = excel.worksheets;
    line = f.readline();
    line = f.readline();
    line = f.readline();

    sheets[0].append(['ts','value'])
    sheets[0].append(['data','float'])

    while line:
        list = []

        line = line.replace(line[9], '#', 1)
        list = line.split()
        list[0] = list[0].replace(list[0][9], ' ', 1)
        for j in range(0, len(list)):
            list[j] = list[j].strip('\n')
        #print(float(list[len(list)-1]))
        x = float(list[len(list)-1])
        list.pop()
        list.append(x)
        sheets[0].append(list)
        line = f.readline()
    i = i + 1
    print(i)
    excel.save('D:\研究生\北京化工\excel2json\\excel'+'\\'+ file[0:len(file)-5] + '.xlsx')


