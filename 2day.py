o=2000
print("------猜字游戏------")
print("输入:1开始游戏")
print("    2结束游戏")
print("当前现金数:",o)
while 1:
    import random
    num = random.randint(0, 10)
    a = input("请输入数字:")
    if a.isdigit():
        a=int(a)
    else:
        continue

    if a == 1:
        if o == 2000:
             print("开始游戏")
        else :
             print("继续游戏,当前现金为：",o)

    elif a == 2 :
          print("现金清零",o - 2000)
          print("游戏结束")
          break

    elif a != 1 and a != 2 :
          print("请输入：1或2")
          print("      1开始游戏")
          print("      2游戏结束")

    if a == 1 :
        while 1 :
            print("请输入10以内的任意数")
            b = input()
            if b.isdigit():
                b=int(b)
                if b == 2:
                    exit()
                if b < 0 or b > 10 :
                    print(end="")
                if b == num and b <= 10 and b >= 0:
                    print("猜对了!")
                    o += 500
                    print("当前现金为:", o)

                elif b != num and b <= 10 and b >= 0:
                    print("猜错了!任意数为", num)
                    o -= 500
                    print("当前现金为:", o)
                if o > 0 :
                    #print("如果想继续请输入“1”")
                    print("如果想结束请输入“2”")

                if o <= 0:
                    print("游戏结束")
                    print("如果想重新开始请输入“3“")
                    print("如果想结束请输入“2”")
                    break

        while 1:
            c = input("请输入数字")
            if c.isdigit():
                c = int(c)
            else:
                continue
            if c == 3:
                print("重新开始")
                o += 2000
                print("当前现金为:", o)
                print("输入:1开始游戏")
                print("    2结束游戏")
                break
            else:
                exit()











