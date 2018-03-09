from rander import rander

# 生成100个不可重复的十进制随机整数
rl1 = rander(quantity=100, minval=0, maxval=100, typed='di', repeat=False)
print(rl1.randlist)
# 生成100个可重复的十进制随机整数
rl2 = rander(quantity=100, minval=0, maxval=50, typed='.di', repeat=True)
print(rl2.randlist)
# 生成100个不可重复的二进制随机整数
rl3 = rander(quantity=100, minval=0, maxval=100, typed='.bi', repeat=False)
print(rl3.randlist)
# 生成100个不可重复的十六进制随机整数
rl4 = rander(quantity=100, minval=0, maxval=100, typed='.hi', repeat=False)
print(rl4.randlist)
# 生成100个不可重复的十进制 .2 浮点数
rl5 = rander(quantity=100, minval=0, maxval=100, typed='.2df', repeat=False)
print(rl5.randlist)
