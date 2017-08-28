import xlwt
import xlrd
import xlutils
import os
from xlutils.copy import copy

f=xlrd.open_workbook("nidongde.xlsx")#读取一个Excel文件到内存
table=f.sheet_by_index(0)
d=xlutils.copy.copy(f)#复制表
w=d.get_sheet(0)                     #定位新的表 使用get_sheet方法
norows=table.nrows
if os.path.exists('nidongde.xlsx'):
    
    print(type(d))
d.save("A.xls")#保存到原来的数据中 
