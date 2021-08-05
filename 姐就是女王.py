import random
print("-------姐就是女王-------")
print("你的随机英雄是：")
pl=0
while 1 :
        a="普通英雄" ; b="稀有英雄" ; c="传奇英雄"
        common = {a: 10};uncommon = {b:30};tale = {c:10}# hero=[common,uncommon,tale]

        sj = random.randint(1, 3)
        jk = {1: common, 2: uncommon, 3: tale}
        print(jk[sj])
        if pl == 0 :
            print("输入1开始游戏")
            print("如果想中途结束游戏请输入9")
        ji=input()
        if sj == 1:
            pl = common[a]
        elif sj == 2:
            pl = uncommon[b]
        elif sj == 3:
            pl = tale[c]

        def add(a, b):
            return a + b
        def adf(a, b):
            return a - b
        if sj == "9" :
            print("游戏结束")
            exit()
        while ji == "1" :
            one=random.randint(0,50)
            two=random.randint(0,50)
            three=random.randint(0,50)
            while 1 :
                print("1.", one,"2.", two,"3.", three)
                ch = input("请选择序号")
                if ch == "1" or ch == "2" or ch == "3" :
                    break
                elif ch != "1" and ch != "2" and ch != "3" :
                    continue

            pi = random.randint(1, 2)

            if ch=="1" and sj==3:
                pl = add(pl, one)
                print(pl)
            elif ch=="2" and sj==3:
                pl = add(pl,two)
                print(pl)
            elif ch=='3' and sj==3:
                pl =add(pl,three)
                print(pl)

            elif ch == "1" and pi==1:
                pl=add(pl,one)
                print(pl)
            elif ch == "2" and pi==1:
                pl = add(pl, two)
                print(pl)
            elif ch == "3" and pi==1:
                pl = add(pl, three)
                print(pl)
            elif ch == "1" and pi==2:
                pl = adf(pl, one)
                print(pl)
            elif ch == "2" and pi==2:
                pl = adf(pl,two)
                print(pl)
            elif ch == "3" and pi==2:
                pl = adf(pl, three)
                print(pl)

            if pl>=100:
                print("victory")
                ss = input ("如果想重新开始请输入1")
                if ss == 1 :
                    continue
                break
            elif pl<=0:
                print("fail")
                exit()




