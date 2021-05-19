import pdfplumber
import xlwt

import os
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title('PDF2EXCEL')
window.geometry('300x30')

def hit_me():
    # 获取文件路径并分拆路径，文件名，扩展名
    file_path = filedialog.askopenfilename()
    file_new = os.path.splitext(file_path)[0]+'.xls'

    # 定义保存excel的位置
    workbook = xlwt.Workbook() #定义workbook
    sheet = workbook.add_sheet('Sheet1') #添加sheet

    i = 0 #Excel起始位置
    log = ''
    pdf = pdfplumber.open(file_path)
    print('\n开始读取数据')
    for page in pdf.pages:
        for table in page.extract_tables():
            for row in table:
                print(row)
                for j in range(len(row)):
                    sheet.write(i,j,row[j])
                i += 1
        print('---------------------------分割线---------------------------')
    pdf.close()

    # 保存excel表
    workbook.save(file_new)
    lbl.configure(text="Convert finished")
# 这里是窗口的内容
lbl = tk.Label(window, text="")
lbl.grid(column=1, row=1)
btn = tk.Button(window,text='Select to convert',command=hit_me)
btn.grid(column=0, row=1)

window.mainloop()