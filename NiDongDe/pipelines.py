# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import xlwt
import xlrd
from xlutils.copy import copy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request  
from scrapy.exceptions import DropItem  
import os

class NidongdePipeline(object):
    
    def __init__(self):
        self.filename = 'nidongde.xlsx'
        self.count = 0
        self.nrows = 0
        if not os.path.exists(self.filename):
            self.f = xlwt.Workbook()
            self.sheet1 = self.f.add_sheet(u'sheet1',cell_overwrite_ok=True)
            row=['番号','名字','图像url']
            for i in range(len(row)):
                self.sheet1.write(0,i,row[i],self.set_style('宋体',220))
            self.count=1
        else :
            self.d = xlrd.open_workbook(self.filename,formatting_info=True)
            self.f = copy(self.d)
            self.sheet1 = self.f.get_sheet(0)
            self.nrows = self.d.sheet_by_index(0).nrows
            
            
    def set_style(self,name,height,bold=False):
        style = xlwt.XFStyle() # 初始化样式
 
        font = xlwt.Font() # 为样式创建字体
        font.name = name # 'Times New Roman'
        font.bold = bold
        font.color_index = 4
        font.height = height
        style.font = font

        return style

    def close_spider(self,spider):
        self.f.save(self.filename)
        
    def process_item(self, item, spider):
        row=[item['name_id'],item['name'],item['pic_url']]
        for i in range(3):
            self.sheet1.write(self.count+self.nrows,i,row[i],self.set_style('宋体',220))
        self.count += 1
        return item


class MyImagesPipeline(ImagesPipeline):
    
     
    def file_path(self, request, response=None, info=None):
        
        image_guid = request.url.split('/')[-1]
        return 'full/%s' % (image_guid)
