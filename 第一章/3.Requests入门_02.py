# 爬取百度翻译接口 -- 带参post请求
import requests

url = "https://fanyi.baidu.com/sug"
query = input("输入一个你要翻译的英文单词：")

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0",
    "Accept": "*/*",
    "Referer": "https://fanyi.baidu.com/mtpe-individual/multimodal",
    "Cookie": "BAIDUID=D7B80668575E51C2140E06CF4DD113C5:FG=1; newlogin=1; BDUSS=Th3bmxBV0hKdEs4WnVBckkxOGMybXBpTEhJdE9LWUJLV1FLVzFiVmRUM2F0SFJvRVFBQUFBJCQAAAAAAAAAAAEAAAAjlFN-wfSyu8H0z-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANonTWjaJ01oN; BDUSS_BFESS=Th3bmxBV0hKdEs4WnVBckkxOGMybXBpTEhJdE9LWUJLV1FLVzFiVmRUM2F0SFJvRVFBQUFBJCQAAAAAAAAAAAEAAAAjlFN-wfSyu8H0z-gAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAANonTWjaJ01oN; BAIDUID_BFESS=D7B80668575E51C2140E06CF4DD113C5:FG=1; __bid_n=197ab3592c792163fe15cd; ab_sr=1.0.1_MGJmZjY1MDhlMDcxYTgzNWE2YmJiMWViZTJiNzI2MWQzNDM3NmJjNzMyMzVkNDQ2YTE5YTA0YmE4YzRmYTYyZjkyMmNhMDcxNDJiMmQ3Yjc4NjE4YjkyZGFmYjI4YmJlODk1YjkwMWM0OWJlZjIxMTM0ODc1ZjNhOGQzOTVkNjVhZTBmYzViNzM1NGU5ZTU5ODFhMmI1OWQ0ODMyOTI2Nw==; RT='z=1&dm=baidu.com&si=21d5ecd0-c95e-4971-b8d3-77da045fbfdb&ss=mceh18jl&sl=7&tt=6pm&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4aup'",
}
# 插入请求体
data = {"kw":query}
resp = requests.post(url,data=data,headers=headers)

# 打印结果,并将服务器返回的内容直接处理为json
print(resp.json())

# 关闭响应
resp.close()