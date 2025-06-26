# 安装requests
# pip install requests

# 国内源
# pip install -i https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple requests

import requests
query = input("输入一个你喜欢的明星：")

url = f'https://cn.bing.com/search?q={query}'

# 添加请求头,模拟浏览器处理一个简单的反爬
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
}

# 获取响应
resp = requests.get(url,headers= headers)

# 获取响应源代码
content = resp.text
# 输出内容
# print(content)

# 将内容写入文件
if(resp.status_code == 200):
    print("请求成功")
    with open('requestTest.html', mode='w', encoding='utf-8') as f:
        f.write(content)
    print("over")
else:
    print("请求失败")