# 1.定位到2023必看电影
# 2.从2023必看片中提取到子页面地址
# 3.请求子页面的链接地址，拿到想要的下载地址

import requests

domain = 'https://dydytt.net/index.htm'

resp = requests.get(domain)
print(resp.text)

resp.close()