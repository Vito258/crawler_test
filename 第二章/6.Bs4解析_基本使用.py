# 安装bs4
# BeautifulSoup
# pip install bs4

# 爬取北京新发地 网页的菜价数据
# 北京新发地的网站改版，所以使用 直接抓包数据就可以
# 由于获取的数据是动态的，所以需要使用post请求

import requests
from bs4 import BeautifulSoup
import csv

domain ='http://www.xinfadi.com.cn/index.html'
get_data_url = 'http://www.xinfadi.com.cn/getCat.html'

resp = requests.post(get_data_url)
# 打印Json数据
# print(resp.json())

# 使用电影天堂网站练习
# 拿到源代码后，使用bs4解析数据
# 1、把页面源代码交给BeautifulSoup 进行处理，生成bs4 对象
dytt_url = 'https://dydytt.net/index.htm'
dytt_resp = requests.get(dytt_url)
dytt_resp.encoding = 'gbk'
dytt_page = BeautifulSoup(dytt_resp.text,'html.parser')

# 从Bs 对象中查找数据
# find(标签,属性 = '')
# find_all(标签,属性 = '')

# 找到最新动漫资源
# 找到目标表格
# 找到包含“最新动漫资源”的 strong 标签
title_strong = dytt_page.find('strong', string='最新动漫资源')

# 找到其父级 div.title_all
parent_div = title_strong.find_parent('div', class_='title_all')

# 找到下一个兄弟 div.co_content8
content_div = parent_div.find_next_sibling('div', class_='co_content8')

# 找到其中的 table
dytt_comic_table = content_div.find('table', border='0', width='100%')


# 从第2行开始，用于抛弃表头
# dytt_comic_table_trs = dytt_comic_table.find_all('tr') [1:]

# 无需舍弃
dytt_comic_table_trs = dytt_comic_table.find_all('tr')


# 创建csv文件
csv_file = open('最新动漫.csv', 'w', encoding='utf-8', newline='')
csv_writer = csv.writer(csv_file)

# 存储最新动漫子页面href
dytt_domain = 'https://dydytt.net'
dytt_comic_hrefs = []
for tr in dytt_comic_table_trs:
    td = tr.find('td')
    if td:
        a_tags = td.find_all('a')
        if len(a_tags) > 1:
            data_a = a_tags[1]
            href_value = data_a['href']  # 获取 href 的值
            csv_writer.writerow([data_a.text, dytt_domain + href_value])  # 写入csv 文件
            dytt_comic_hrefs.append(dytt_domain + href_value)

resp.close()
dytt_resp.close()