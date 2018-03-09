# rander
Generate a randomized sequence of numbers

# Env
Python 3.X

# Install
```
pip install rander
```
## or

```
git clone git@github.com:15281029/rander.git
cd rander
python setup.py install
```

# Usage
- 可设置随机数个数，类型，最大/最小值，是否可重复

```
        quantity    生成随机数的个数
        minval      生成随机数的最小值
        maxval      生成随机数的最大值
        typed       生成随机数的类型
            -'i'    整数
            -'f'    浮点数
            -'.1f'  一个小数位的浮点数
            -'.nf'  n个小数位的浮点数(最大9)

            -'b'    二进制
            -'d'    十进制
            -'o'    八进制
            -'h'    十六进制

            eg.
                typed='di'      十进制整数
                      '.2df'    十进制带两位小数位的浮点数
        repeat      数字是否可重复
```

# eg.

```
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
```
