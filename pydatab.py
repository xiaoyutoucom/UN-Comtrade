import json
import urllib
import urllib.request
from urllib.error import URLError
from random import randint
import random
import time
import os 
import requests
from requests import exceptions
import  json
import csv
import tablib
USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    ]
proxy={'http':'222.74.202.229:8080'}

list1 = []
def download_url(url, path, header,count):
    """
    函数功能:下载url链接内容到path路径下
    参数解释:
        url: 下载链接
        path: 本地保存路径
        header: 设置访问用户代理{'http':'43.243.166.221:8080'},
        {'http':'124.205.155.150:9090'},
        {'http':'14.215.224.254:3128'},
        {'http':'221.226.94.218:110'},
         {'http':'124.205.155.155:9090'},
         ,{'http':'116.196.88.86:3128'},
             
       
    """
    proxy_list=[
        {'http':'222.74.202.229:8080'},
        {'http':'74.143.245.221:80'},
    
        {'http':'123.139.56.238:9999'},
        {'http':'218.91.138.184:32694'},
        {'http':'49.76.159.169:32736'},
        {'http':'221.226.94.218:110'}
  
        ]
    global list1
    keep_request = True
    alcount = 0
    while keep_request:
     try:
       
        # 代码
        # proxy = random.choice(proxy_list)
        # print("代理"+str(proxy))
        print("Downing from " + url )
        global proxy
        print(count)
        print(alcount)
     
        alcount +=1
        
        
        #, proxies= proxy
        #print('获取的代理 '+str(proxy))暂时取消代理
        content = requests.get(url,timeout=40, headers=header)
        #content = requests.get(url,timeout=20, headers=header, proxies= proxy)
        #time.sleep(100)
        print(str(content)+"返回是否正确")
        json_str=json.dumps(content.text)
        #print(json_str+"cccccc")
        state=json.loads(content.text)
        #print(state)
        #print(state['dataset']) 

        dataset = state['dataset']
        print(str(len(dataset))+"  数据长度")
        if len(dataset):
            for i in range(0, len(dataset)):
                print(str(dataset[i])+"  这条有数值")
                list1.append(dataset[i])

        print(str(len(list1))+"  list1数据长度")
        # 将 Python 字典类型转换为 JSON 对象
        
       
        # with open(path,'ab') as outfile:
           #  outfile.write(content.content)
        
        """
        httpproxy_handler = urllib.request.ProxyHandler(proxy)

        opener = urllib.request.build_opener(httpproxy_handler)
        content = urllib.request.Request(url, headers=header)
        response = opener.open(content)
        with urllib.request.urlopen(content) as file:
            with open(path,'wb') as outfile:
                outfile.write(file.read())"""

        # 请求成功，修改标识
        keep_request = False
     except exceptions.Timeout as e:
        print("访问超时错误，等待重试2  ______________________________")
        
        count = 99
     except URLError:
        # 遇到错误，等待
        print("遇到错误，等待重试  ______________________________")
        
        count = 99
     except Exception as e: print(e)
     except:
         # 遇到错误，等待
        print("遇到错误，等待重试all  ______________________________")
        
        count = 99
"""
    content = urllib.request.Request(url, headers=header)
    with urllib.request.urlopen(content) as file:
        with open(path,'wb') as outfile:
            outfile.write(file.read())"""
 
def main():
    random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
    header = {'User-Agent':random_agent}
    
    #-----------------获取所有国家的名单和国家对应编码号-----------------
    """
    if not os.path.exists("./reporterAreas.json"):
        download_url("https://comtrade.un.org/Data/cache/reporterAreas.json","./reporterAreas.json",header)
    with open('reporterAreas.json', 'r',encoding='utf_8_sig') as f:
         data = json.load(f)
    results = data.get("results")
    id = [] #存放国家编码号
    text = [] #存放国家名称
    for i in results:
        id.append(i.get("id"))
        text.append(i.get("text"))
        # 删除第一个元素，第一个元素是all
        new_id = id[1:]
    """
    
    id = [156] #存放r国家编码号 改为只能写一个
    text = ['China'] #存放r国家名称  改为只能写一个
    #pid = [360,458,608,764,702,96,116,104,704,418]#存放p国家编码号
    #ptext = ['Indonesia','Malaysia','Philippines','Thailand','Singapore','Brunei Darussalam','Cambodia','Myanmar','Viet Nam','Lao People'] #存放p国家名称
    #pid = [360]
    pid = ['360,458,608,764,702','96,116,104,704,418','496,762,498,504,31','144,524,64,422,376','887,634,48,410,818','710,450,231,554,591','834']#存放p国家编码号  每五个一组
    #pid = [496]#存放p国家编码号
    #不需要这个了ptext = ['Indonesia','Malaysia','Philippines','Thailand','Singapore','Brunei Darussalam','Cambodia','Myanmar','Viet Nam','Lao People','蒙古国','塔吉克斯坦','摩尔多瓦','摩洛哥','阿塞拜疆','斯里兰卡','尼泊尔','不丹','黎巴嫩','以色列','也门','卡塔尔','巴林','韩国','埃及','南非','马达加斯加','埃塞俄比亚','新西兰','巴拿马','坦桑尼亚'] #存放p国家名称
    #cc=[4403,4406,4407,4408,4409,4410,4411,4412,4413,4701,4702,4703,4704,4705,4706,4414,4415,4416,4417,4418,4419,4420,4421,4401,4402,4404,4405,48,4707,940161,940169,940330,940340,940350,940360]#存放行业
    cc=['4403,4406,4407,4408,4409','4410,4411,4412,4413,4701','4702,4703,4704,4705,4706','4414,4415,4416,4417,4418','4419,4420,4421,4401,4402','4404,4405,48,4707,940161','940169,940330,940340,940350,940360']#存放行业 每五个一组
    # 若运行中断，继续下载仅需要更改下面三个参数
    start_year = '2010'#可以选择多年  '2010,2011,2012,2013,2014' 最多五年
    #stop_year = 2010
    begin_id = 0 #当前年份已下载文件数目
    begin_cc = 0 #当前年份已下载文件数目
    # 创建data文件夹存放下载数据
    count = 0 # 代理下载次数
    ip_update = 99 #代理更换频率，每访问ip_update次更换新代理
    
    #for year in range(start_year, stop_year+1):
        # 创建年份文件夹将数据按年份分开存放
       
        
    for i in range(begin_id, len(pid)):
            for itemc in range(begin_cc, len(cc)):
                random_agent = USER_AGENTS[randint(0, len(USER_AGENTS)-1)]
                print(random_agent)
                header = {'User-Agent':random_agent}
                
                url = "http://comtrade.un.org/api/get?r=" + str(id[0])+"&p="+str(pid[i]) + "&ps="+str(start_year) + "&px=H3&rg=all&freq=A&type=C&cc=" + str(cc[itemc]) + "&fmt=json"
                path = ""
                
                download_url(url,path,header,count)
                print("Done")
        
                count += 1
                # 暂停36秒，保证一小时访问100次
                #time.sleep(36)
    global list1
    print(str(len(list1))+"  list1数据长度")
    with open("./保存数据文件15-19.json",'w',encoding='utf-8') as json_file:
        json.dump(list1,json_file,ensure_ascii=False)
    # 将json中的key作为header, 也可以自定义header（列名）
    header=tuple([ i for i in list1[0].keys()])
    data = []
    # 循环里面的字典，将value作为数据写入进去
    for row in list1:
        body = []
        for v in row.values():
            body.append(v)
        data.append(tuple(body))
    #将含标题和内容的数据放到data里
    data = tablib.Dataset(*data,headers=header)
    #写到桌面
    open("./保存数据文件"+str(start_year) + ".xls", 'wb').write(data.xls)
      


if __name__ == '__main__':
    main()
    print("运行成功")

