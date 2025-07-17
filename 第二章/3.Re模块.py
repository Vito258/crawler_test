import re
# findall 匹配字符串中所有内容，并返回数组
# 注意前面加了 r，即：r"\d+"，这样 \d 就不会被当作非法转义序列处理了。
# 将正则表达式字符串改为 原始字符串（raw string），告诉 Python 不要对反斜杠进行转义：
lst  = re.findall(r"\d+","我的电话号是：12345678，女朋友的电话是：987654321")
print(lst)

print("---------------------------------------")
# finditer 匹配字符串中所有内容，并返回迭代器
it = re.finditer(r"\d+","我的电话号是：12345678，女朋友的电话是：987654321")
for i in it:
    print(i.group())

print("---------------------------------------")
# search 匹配字符串中第一个内容，并返回对象
s = re.search(r"\d+","我的电话号是：12345678，女朋友的电话是：987654321")
print(s.group())

# match 匹配字符串开头的内容，并返回对象
# 默认是正则表达式之前加了一个^, match 方法从字符串的开头开始匹配，如果匹配成功，则返回相应的匹配对象，否则返回 None。
m = re.match(r"\d+","12345678，女朋友的电话是：987654321")
print(m.group())

print("---------------------------------------")
# 预加载正则表达式
obj = re.compile(r"\d+")
s1 = obj.search("我的电话号是：12345678，女朋友的电话是：987654321")
print(s1.group())

print("=========================")
string = """
<div class='jay'><span id= '1'>周杰伦</span></div>
<div class='jj'><span id= '2'>林俊杰</span></div>
<div class='eason'><span id= '3'>陈奕迅</span></div>
"""
obj = re.compile(r"<div class='.*?'><span id= '\d+'>.*?</span></div>", re.S) # re.S 忽略换行符
result = obj.finditer(string)
for i in result:
    print(i.group())

print("=========================")
# (?P<分组名称>正则)可以单独从正则匹配的内容中进一步提取特定的值
# 给特定的值的部分添加一个括号，括号里面可以起一个名字，名字可以任意，但是名字不能重复，这个名字会作为匹配对象的属性，属性名就是括号里面定义的名字。
obj = re.compile(r"<div class='.*?'><span id= '(?P<id>\d+)'>(?P<wahaha>.*?)</span></div>", re.S) # re.S 忽略换行符
result = obj.finditer(string)
for i in result:
    print(i.group("id")+ ":" + i.group("wahaha")) # 获取属性