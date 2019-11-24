product_list = [
    ( "电脑", 1999),
    ( "鼠标", 10),
    ( "游艇", 20),
    ( "美女", 998),]
shopping_list = []
salary = input("请输入您的工资:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index,item in enumerate(product_list):
            print(index,item)
        user_choice = input("请选择商品,退出请输入q:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(product_list) and user_choice >= 0:
                p_item = product_list[user_choice]
                if p_item[1] <= salary:
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("添加商品：%s到你的购物车，您当前的余额是：%s"%(p_item,salary))
                else:
                    print("您的余额不足...")
            else:
                print("您选择的商品不存在...")
        elif user_choice == 'q' or 'Q':
            print("----------购物车列表---------")
            for p in shopping_list:
                print(p)
            print("您的余额是：",salary)
            exit()
        else:
            print("错误选项")
else:
    print("请输入数字")
