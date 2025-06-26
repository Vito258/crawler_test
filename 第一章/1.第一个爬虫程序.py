# 导入包
from urllib.request import urlopen

url = 'http://www.baidu.com'

# 打开一个网址得到相应
resp = urlopen(url)

# 读取响应内容并解码
content = resp.read().decode('utf-8')

# 在相应里面读取内容
print(content)

# 将内容写入文件
with open('myBaidu.html', mode='w', encoding='utf-8') as f:
    f.write(content)
print("over")
