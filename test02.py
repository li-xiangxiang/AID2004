"""
设置format()参数的值
"""
# 1.直接在format()中进行赋值
str01 = "学校：{name},网址：{url}".format(name="达内", url="tts.tmooc,cn")
print(str01)
# 2.通过传递多值参数向format传递参数进而对{}进行赋值
# 使用**传递字典
dict01 = {"name": "达内", "url": "tts.tmooc,cn"}
str02 = "学校：{name},网址：{url}".format(**dict01)
print(str02)
# 传递列表
list01 = ["达内", "tts.tmooc,cn"]
str03 = "学校：{0[0]}, 网址：{0[1]}".format(list01)
print(str03)
# 传递多个列表
list02 = ["百度", "tts.tmooc,cn"]
list03 = ["达内", "http:www.baidu.com"]
str04 = "学校：{1[0]}, 网址：{0[1]}".format(list02, list03)
print(str04)
# 传入对象
class Cat:
    def __init__(self, name):
        self.name = name
class Mouse:
    def __init__(self, name):
        self.name = name
tom = Cat("Tom")
jerry = Mouse("Jerry")
str05 = "{0.name} want to eat {1.name}".format(tom, jerry)
print(str05)
