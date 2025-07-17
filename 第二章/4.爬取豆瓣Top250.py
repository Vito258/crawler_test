# 拿到页面源代码
# 通过Re来提取到想要的有用信息
import requests
import re
url = "https://movie.douban.com/top250"

# 重新封装参数
params = {
    "type": 24,
    "interval_id": "100:90",
    "action": "",
    "start": 0,
    "limit": 20
}

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",

}
resp = requests.get(url,headers= headers)
page_content = resp.text

obj = re.compile(r'<div.*?class="hd">.*?<span class="title">(?P<name>.*?)</span>.*?'
                        r'<p>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)</span>',re.S)
douban_it = obj.finditer(page_content)
for it in douban_it:
    print(it.group("name"),it.group("year").strip(),it.group("score"),it.group("num"))