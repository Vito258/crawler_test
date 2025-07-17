# 拿到页面源代码
# 通过Re来提取到想要的有用信息
import requests
import re
import csv
url = "https://movie.douban.com/top250"

# 添加请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0",

}
resp = requests.get(url,headers= headers)
page_content = resp.text

#
obj = re.compile(r'<div.*?class="hd">.*?<span class="title">(?P<name>.*?)</span>.*?'
                        r'<p>.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>.*?<span>(?P<num>.*?)</span>',re.S)
douban_it = obj.finditer(page_content)

# 打印数据
# for it in douban_it:
#     print(it.group("name"),it.group("year").strip(),it.group("score"),it.group("num"))

# 写入csv文件
with open("data.csv", "w", encoding="utf-8", newline='') as f:  # 使用 with 自动管理文件，并指定 newline
    csv_writer = csv.writer(f)
    for i in douban_it:
        dic = i.groupdict()
        dic["year"] = dic["year"].strip()

        # dic["name"] = dic["name"]
        # dic["score"] = dic["score"]
        # dic["num"] = dic["num"]
        values = list(dic.values())  # 转换为列表

        # 调试：打印数据检查
        print("待写入数据:", values)

        # 确保数据有效
        if any(values):  # 检查非空
            try:
                csv_writer.writerow(values)
            except Exception as e:
                print(f"行写入失败: {e}")

f.close()
resp.close()
print("over")