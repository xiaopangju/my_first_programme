# 收集用户数据
mcbbs_username = str(input("请输入您的 mcbbs 用户名："))
mcbbs_uid = str(input("请输入您的 mcbbs uid："))
mcbbs_password = input("请输入您的 mcbbs 密码：")
# 判断用户是不是混乱
if mcbbs_uid == "3038":
    if mcbbs_username == "混乱":
# 打印出混乱专属结果
        print("你竟然是混乱！")
else:
# 打印其他用户最终结果
    print("哈哈，你被骗了！你的用户名是：" + mcbbs_username + "\n你的密码是：" + mcbbs_password + "\n你的uid是：" + mcbbs_uid + "。")
# 有人建议我优化上面一行代码，但是我就是不优化，lueluelue