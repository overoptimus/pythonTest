def save_file(boy, girl, i):
    try:
        with open('boy_' + str(i) + '.txt', mode='w') as boy_file:
            boy_file.writelines(boy)
        with open('girl_' + str(i) + '.txt', mode='w') as girl_file:
            girl_file.writelines(girl)
    except OSError as reason:
        print('出错了', reason)

def split_file(file_name):
    boy = []
    girl = []
    i = 1
    try:
        with open(file_name) as record:
            for each_record in record:
                if each_record[:6] != '======':
                    (role, inform) = each_record.split(':', 1)
                    if role == '小甲鱼':
                        boy.append(inform)
                    elif role == "小客服":
                        girl.append(inform)
                else:
                    # 文件分别保存
                    save_file(boy, girl, i)
                    i += 1
                    boy.clear()
                    girl.clear()
            save_file(boy, girl, i)
    except OSError as reason:
        print('出错了', reason)



split_file('record.txt')
