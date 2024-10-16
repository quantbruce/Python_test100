94.题目：时间函数举例4,一个猜数游戏，判断一个人反应快慢。


#### My Method

import time
import random

def guess_num():
    x = input("do you want to play this game?('y' or 'n')")
    if x == 'y':
        start = time.clock()
        guess = int(input('please input a number = '))
        sys = int(random.randint(0, 2**32) % 100)
        while guess != sys:
            if guess > sys:
                guess = int(input('please input a little number = '))
            elif guess < sys:
                guess = int(input('please input a bigger number = '))
        if guess == sys:
            print('Conguratulation! you are right!')
            print('the right answer is %d' % sys)
        end = time.clock()
        time_interval = end - start
        print('the total time you spend is %.6f' % time_interval)
        if time_interval < 15:
            print('you are so clever!')
        elif time_interval < 25:
            print('you are normal!')
        else:
            print('you are stupid!')
    else:
        print('get out! you are 闹太套!')
        return


guess_num()
