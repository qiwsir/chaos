"""
author:文欣薇
data：2020.10.21
subject:猜数游戏
"""

import random
n = random.randint(1,100)                                 #定义n为产生100以内的随机整数
i = 0                                                     #定义i为猜测的次数
flag = True
while flag:
    guess = int(input("不妨来猜一下100以内的整数："))       #定义guess来存储用户输入数字     //    如果用户输入的数字超过了前面程序随机生成的，应该进行判断，并给予提示。
    i += 1                                                #执行循环一次，i增加1，计数猜测次数
    if guess == n:
        print("太厉害了，猜对啦！") 
        flag = False                             # 这样功能能够实现，但是，需要程序还要进行判断。浪费计算了。建议使用break语句。
    elif guess > n:
        print("大了！继续猜，猜对有奖哦！")
    else:
        print("小了！继续猜，猜对有奖哦！")
                
print('\n你一共猜了'+str(i)+'次。猜对了也没奖，游戏结束！')






