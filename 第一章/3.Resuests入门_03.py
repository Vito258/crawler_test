# 爬取豆瓣排行榜接口 -- 带参get请求
import requests

# 定义url
url = "https://movie.douban.com/j/chart/top_list" # ?type=24&interval_id=100%3A90&action=&start=0&limit=20

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
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36",

}
resp = requests.get(url, params=params,headers= headers)

print(resp.json())

# 关闭响应
resp.close()