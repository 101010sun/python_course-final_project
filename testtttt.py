# coding=utf-8
import pandas as pd
import os
import matplotlib.pyplot as plt
import math
import seaborn as sns
import numpy as np
#相關係數
def mean(x):
    return sum(x) / len(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    deviations = de_mean(x)
    variance_x = 0
    for d in deviations:
        variance_x += d**2
    variance_x /= len(x)
    return variance_x


def dot(x, y):
    dot_product = sum(v_i * w_i for v_i, w_i in zip(x, y))
    dot_product /= (len(x))
    return dot_product

def correlation(x, y):
    variance_x = variance(x)
    variance_y = variance(y)
    sd_x = math.sqrt(variance_x)
    sd_y = math.sqrt(variance_y)
    dot_xy = dot(de_mean(x), de_mean(y))
    return dot_xy/(sd_x*sd_y)

path=r'C:\\Users\\umin3\\Desktop\\python\\pyclass\\culture' #要試的話路徑記得改
year=[]
times=[]
salary=[]
#東西南北經濟成長率
east = []
west = []
south = []
north = []
#藝文活動種類
visual_art = []
craft = []
design = []
music = []
drama = []
dance = []
rap = []
video = []
folklore = []
language_book = []
variety_show = []
#產業結構
agriculture = []
industry = []
service_industry = []
financial_intermediary = []
insurance = []
securities_futures = []

csvfile={}
money_data=pd.read_csv('C:\\Users\\umin3\\Desktop\\python\\pyclass\\money\\國內主要經濟指標(按年度).csv', encoding = 'utf-8')
for root,dirs,files in os.walk(path):#os.walk用來取得指定資料夾內所有檔案、子資料夾內所有檔案的資訊。
    for file in files:#files為檔案名稱的迭代器，遍歷它以取得檔案名來開檔
        csvfile[file]= pd.read_csv('C:\\Users\\umin3\\Desktop\\python\\pyclass\\culture\\'+file)#利用dictionary的語法，將檔案名稱當Key來儲存讀入csv檔的dataframe
        
        year.append(csvfile[file].iloc[0,0])
        times.append(csvfile[file].iloc[0,2])
        
        east.append(csvfile[file].iloc[23,2])
        west.append(csvfile[file].iloc[10,2])
        south.append(csvfile[file].iloc[16,2])
        north.append(csvfile[file].iloc[2,2])
        
        visual_art.append(csvfile[file].iloc[0,4])
        craft.append(csvfile[file].iloc[0,5])
        design.append(csvfile[file].iloc[0,6])
        music.append(csvfile[file].iloc[0,7])
        drama.append(csvfile[file].iloc[0,8])
        dance.append(csvfile[file].iloc[0,9])
        rap.append(csvfile[file].iloc[0,10])
        video.append(csvfile[file].iloc[0,11])
        folklore.append(csvfile[file].iloc[0,12])
        if(file == '101.csv' or file == '102.csv'):
            language_book.append(csvfile[file].iloc[0,14]+csvfile[file].iloc[0,13])
            variety_show.append(csvfile[file].iloc[0,15])
        else:
            language_book.append(csvfile[file].iloc[0,13])
            variety_show.append(csvfile[file].iloc[0,14])

        for i in range(len(money_data['年度'])):
            if money_data['年度'][i] == csvfile[file].iloc[0,0]:
                salary.append(money_data['平均每人國民所得毛額（美元）'][i])
                agriculture.append(money_data['產業結構（按各產業GDP比重）-農業'][i])
                industry.append(money_data['產業結構（按各產業GDP比重）-工業'][i])
                service_industry.append(money_data['產業結構（按各產業GDP比重）-服務業'][i])
                financial_intermediary.append(money_data['產業結構（按各產業GDP比重）-服務業-金融中介業'][i])
                insurance.append(money_data['產業結構（按各產業GDP比重）-服務業-保險業'][i])
                securities_futures.append(money_data['產業結構（按各產業GDP比重）-服務業-證券期貨及其它金融業'][i])
        pass
finaldf=pd.DataFrame({"年":year,"展演數":times,"所得":salary,"農業":agriculture,"工業":industry,"服務業":service_industry,"金融中介業":financial_intermediary,"保險業":insurance,"證券期貨及其它金融業":securities_futures})
localdf = pd.DataFrame({"年":year,"東部展覽數":east,"中部展覽數":west,"北部展覽數":north,"南部展覽數":south})
actaldf = pd.DataFrame({"年":year,"視覺藝術":visual_art,"工藝":craft,"設計":design,"音樂":music,"戲劇":drama,"舞蹈":dance,"說唱":rap,"影片":video,"民俗":folklore,"語言與圖書":language_book,"綜藝":variety_show})
coraldf = pd.Series({"視覺藝術相關性":correlation(salary,visual_art),"工藝相關性":correlation(salary,craft),"設計相關性":correlation(salary,design),"音樂相關性":correlation(salary,music),"戲劇相關性":correlation(salary,drama),"舞蹈相關性":correlation(salary,dance),"說唱相關性":correlation(salary,rap),"影片相關性":correlation(salary,video),"民俗相關性":correlation(salary,folklore),"語言與圖書相關性":correlation(salary,language_book),"綜藝相關性":correlation(salary,variety_show)})

plt.plot('年','展演數',data=finaldf,color = '#53868B') #所得和展覽數折線圖
plt.plot('年','所得',data=finaldf,color = '#F08080')
plt.legend()
plt.title("展覽樹和所得曲線圖")
plt.xlabel("年度")
plt.ylabel("展覽次數/所得")
plt.show()

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
plt.bar(localdf['年']-0.15,localdf['東部展覽數'],label='東部地區',width=width) #推疊長條圖
plt.bar(localdf['年']+0.15,localdf['北部展覽數'],label='北部地區',width=width)
plt.bar(localdf['年']-0.05,localdf['南部展覽數'],label='南部地區',width=width)
plt.bar(localdf['年']+0.05,localdf['中部展覽數'],label='中部地區',width=width)
plt.plot('年','所得',data=finaldf,color = '#F08080')
plt.legend() #顯示圖表的label
plt.title("各地區年度藝文活動次數比較")
plt.xlabel("年度")
plt.ylabel("展覽次數")
plt.show() #跳出圖表


plt.plot(coraldf)

plt.title("所得與各項藝文活動相關係數圖")
plt.xlabel("藝文活動種類")
plt.ylabel("相關係數")
plt.show() #跳出圖表