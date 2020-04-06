goods_list = []
cost_dic = {'наименование': '', 'цена': '', 'количество': '', 'единицы': ''}
analytics_list = {'наименование': [], 'цена': [], 'количество': [], 'единицы': []}
num = 0
feature_ = None
control = None
while True:
    stop = input("Хотите внести еще один товар (да/нет) ")
    if stop == 'нет':
        for key, value in analytics_list.items():
            print(f"{key} : {value}")
        break
    num += 1
    if stop == 'да':
        for f in cost_dic.keys():
            feature_ = input(f'Input feature "{f}"')
            cost_dic[f] = int(feature_) if (f == 'price' or f == 'quantity') else feature_
            analytics_list[f].append(cost_dic[f])
        goods_list.append((num, cost_dic))
