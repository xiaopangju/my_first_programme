#引入
import webbrowser
import time
url = 'https://www.bilibili.com/video/BV1GJ411x7h7/'
input("你获得了一份大礼。敲击回车以领取！")
input("首先，输入你的KLPBBS UID：")
input("然后，给出你的用户名：")
print("享受你的大礼吧！")

time.sleep(5)

webbrowser.open_new_tab(url)

time.sleep(4)
print("哈哈，你被骗了！")