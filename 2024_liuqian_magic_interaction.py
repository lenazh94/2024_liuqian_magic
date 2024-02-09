from collections import deque
import random

def get_input(prompt_message, expected_type=int, min_val=None, max_val=None):
    while True:
        user_input = input(prompt_message)
        try:
            value = expected_type(user_input)
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"范围错误，请输入 {min_val}至{max_val}之间的整数。")
            else:
                return value
        except ValueError:
            print("输入类型错误，请重新输入要求范围内的整数。")

# 获取名字字数，地域，性别
name = get_input("请输入名字字数，范围2-7：", int, 2, 7)
location = get_input("南方人请输入1，北方人请输入2，不确定请输入3：", int, 1, 3)
sexe = get_input("男生请输入1，女生请输入2：", int, 1, 2)

def simulate_magic(name, location, sexe):
    # 洗牌
    cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
    random.shuffle(cards)

    # 随机选择四张，对折撕开
    selected_values = random.sample(cards, 4)
    selceted_cards = deque(selected_values * 2)
    print(f"抽出的牌：{selceted_cards}")
    
    # 1. 根据名字有几个字，将前n张牌移到最后
    selceted_cards.rotate(-name)

    # 2. 取出前三张牌并随机插入剩余牌中，不能插在第一张和最后一张
    first_three = [selceted_cards.popleft() for _ in range(3)]

    for card in first_three:    
        insert_position = random.randint(1, len(selceted_cards) - 2)
        selceted_cards.insert(insert_position, card)

    # 3. 把最上面的牌放到一边
    remembered_card = selceted_cards.popleft()

    # 4. 南方人取1张，北方人取2张，无法确定取3张，将这些牌随机插入剩下的牌中
    first_a = [selceted_cards.popleft() for _ in range(location)]


    for card in first_a:
        if len(selceted_cards) > 2:
            insert_position = random.randint(1, len(selceted_cards) - 2)
        else:
            insert_position = 0
        selceted_cards.insert(insert_position, card)

    # 5. 男生取1张，女生取2张，将这些牌扔掉
    for _ in range(sexe):
        selceted_cards.popleft()

    # 6. 见证奇迹的时刻
    selceted_cards.rotate(-7)

    # 7. 好运留下来，烦恼丢出去！
    while len(selceted_cards) > 1:
        selceted_cards.append(selceted_cards.popleft())  # 第一张牌移到最后
        selceted_cards.popleft()  # 删除现在的第一张牌

    # 返回手里剩下的牌和放在一边的牌
    return selceted_cards[0], remembered_card

final_card, remebered_card = simulate_magic(name, location, sexe)

print(f"初始牌：{remebered_card}, 剩下的牌：{final_card}")
print(f"初始牌和手里的牌是否相同：{remebered_card == final_card})"
print()
print("祝大家龙年大吉！")
