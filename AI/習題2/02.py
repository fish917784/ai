#參考chatgpt
import random
import copy

# 定義城市的坐標
citys = [ 
    (0,3),(0,0),
    (0,2),(0,1),
    (1,0),(1,3),
    (2,0),(2,3),
    (3,0),(3,3),
    (3,1),(3,2)
]

# 初始化訪問順序
path = [i for i in range(len(citys))]

# 計算兩個點之間的距離
def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

# 計算訪問所有城市的總距離
def pathLength(p):
    dist = 0
    plen = len(p)
    for i in range(1,plen):
        dist += distance(citys[p[i-1]], citys[p[i]])
    return dist

# 爬山演算法
def climb():
    router = path
    length = len(path)
    distance = pathLength(path)

    turn = 1000
    while turn:
        # 隨機選擇兩個不同的城市進行交換
        p1 = int(random.random() * length)
        p2 = int(random.random() * length)
        while p1 == p2:
            p2 = int(random.random() * length)

        new = copy.deepcopy(router)
        new[p1],new[p2] = new[p2],new[p1]
        curr_distance = pathLength(new)
        if curr_distance < distance:
            distance = curr_distance
            router = new
        turn -= 1

    print("climb總距離：", distance)
    return router

# 執行爬山演算法並輸出結果
print(climb())
