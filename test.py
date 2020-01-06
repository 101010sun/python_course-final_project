import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] #顯示中文
plt.rcParams['axes.unicode_minus'] = False
path=r'D:\python\python-project\culture' #要試的話路徑記得改
year=[]
times=[]
salary=[]
east=[]
north=[]
south=[]
west=[]
csvfile={}
money_data=pd.read_csv('D:\\python\\python-project\\money\\國內主要經濟指標(按年度).csv',encoding='utf-8')
for root,dirs,files in os.walk(path):#os.walk用來取得指定資料夾內所有檔案、子資料夾內所有檔案的資訊。
    for file in files:#files為檔案名稱的迭代器，遍歷它以取得檔案名來開檔
        csvfile[file]= pd.read_csv('D:\\python\\python-project\\culture\\'+file,encoding='utf-8')#利用dictionary的語法，將檔案名稱當Key來儲存讀入csv檔的dataframe
        year.append(csvfile[file].iloc[0,0]) #年
        times.append(csvfile[file].iloc[0,2]) #每年總展覽數
        east.append(csvfile[file].iloc[23,2]) #東部
        west.append(csvfile[file].iloc[10,2]) #中部
        south.append(csvfile[file].iloc[16,2]) #南部
        north.append(csvfile[file].iloc[2,2]) #北部
        for i in range(len(money_data['年度'])):
            if money_data['年度'][i] == csvfile[file].iloc[0,0]:
                salary.append(money_data['平均每人國民所得毛額（美元）'][i])
        pass
finaldf=pd.DataFrame({"年":year,"展覽數":times,"所得":salary})
localdf=pd.DataFrame({"年":year,"東部展覽數":east,"中部展覽數":west,"南部展覽數":south,"北部展覽數":north}) #地區表格

plt.bar(localdf['年'],localdf['東部展覽數'],label='東部地區') #推疊長條圖
plt.bar(localdf['年'],localdf['北部展覽數'],label='北部地區',bottom=localdf['東部展覽數'])
plt.bar(localdf['年'],localdf['南部展覽數'],label='南部地區',bottom=localdf['北部展覽數'])
plt.bar(localdf['年'],localdf['中部展覽數'],label='中部地區',bottom=localdf['南部展覽數'])
plt.legend() #顯示圖表的label
plt.title("各地區年度藝文活動次數比較")
plt.xlabel("年度")
plt.ylabel("展覽次數")
plt.show() #跳出圖表

width = 0.1
plt.bar(localdf['年']-0.15,localdf['東部展覽數'],label='東部地區',width=width,color='peachpuff') #推疊長條圖
plt.bar(localdf['年']-0.05,localdf['中部展覽數'],label='中部地區',width=width,color='sandybrown')
plt.bar(localdf['年']+0.05,localdf['南部展覽數'],label='南部地區',width=width,color='navajowhite')
plt.bar(localdf['年']+0.15,localdf['北部展覽數'],label='北部地區',width=width,color='peru')
plt.plot(finaldf['年'],finaldf['所得'],label='平均所得',linewidth=3,color='green') #所得和展覽數折線圖
plt.legend() #顯示圖表的label
plt.title("各地區年度藝文活動次數比較")
plt.xlabel("年度")
plt.ylabel("展覽次數/平均所得")

plt.show() #跳出圖表