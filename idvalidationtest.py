import time
def check_id_length(n):
    if len(str(n)) != 18:
        print("只支持18位身份证号查询")
        return False
    else:
        return True

def check_id_data(n):
    n = str(n)
    n2 = str(n[:16])
    time_now = int(time.strftime("%Y",time.localtime()))
    is_digit = (not(n2.isdigit())) or (not(n[17].isdigit()) and (n[17]) !="x")
    if (is_digit):
        print("对不起，您这是火星身份证，暂不受理")
    elif (int(n[6:10]))>time_now:
            print(n[6:10],"年的人？您是穿越回来吗？")
    elif (int(n[10:12]))>12:
        print(n[10:12],"月出生？,您是捡来的吧!!")
    elif (int(n[12:14]))>31:
        print(n[12:14],"日出生？,您一定是充话费送的")
    else:
        check_id_data2(n)
def check_id_data2(n):
        var=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        var_id=['1','0','x','9','8','7','6','5','4','3','2']
        sum = 0
        if int(n[16])%2==0:
            gender="女"
            same=int(int(n[16])/2)
        else:
            gender="男"
            same=int((int(n[16])+1)/2)
        for i in range(0,17):
            sum += int(n[i])*var[i]
        sum %= 11
        if (var_id[sum])==str(n[17]):
            print("身份证号规则核验通过，校验码是：",var_id[sum])
            print("出生于：",n[6:10],"年",n[10:12],"月",n[12:14],"日","性别：",gender,"\n当地同性别同生日排名：",same)
            return sum
        else:
            print("出生于：",n[6:10],"年",n[10:12],"月",n[12:14],"日","性别：",gender,"\n当地同性别同生日排名：",same)
            print("但身份证号规则核验失败，校验码应为",var_id[sum],"，当前校验码是：",n[17])
            return 0
while(1):
    print("\n菜单，请输入数字\n----------------------")
    print("输入1手动输入身份证号")
    print("输入2选择测试号")
    print("不然就拜拜")
    print("----------------------")
    select = input("\n请输入：")
    if (select.isdigit()):
        pass
    else:
        print("说好的输入数字的呢，拜拜了您嘞")
        break
    select = int(select)
    if (select == 1):
        n = input("请输入18位身份证号:")
        if check_id_length(n):
            check_id_data(n)
        else:
            print("请重新输入")
    elif select == 2:
                 print("\n----------------------")
                 print("开始校验身份证号：61011519920317602")
                 check_id_length(61011519920317602)
                 print("\n----------------------")
                 print("开始校验身份证号：610115199203176021")
                 check_id_data(610115199203176021)
                 print("\n----------------------")
                 print("开始校验身份证号：610115199203176028")
                 check_id_data(610115199203176028)
    else:
                 break
