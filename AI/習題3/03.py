import random

# 初始化變量和目標函數值
vars = [0.0, 0.0, 0.0]
value = 0.0
fails = 0

# 目標函數及約束條件檢查
def f(vars):
    x, y, z = vars
    if x + y <= 10 and 2*x + z <= 9 and y + 2*z <= 11 and x >= 0 and y >= 0 and z >= 0:
        return 3*x + 2*y + 5*z
    else:
        return -1

# 主過程
if __name__ == "__main__":
    while fails < 10000:
        # 生成新變量組合
        newVars = vars.copy()
        for i in range(len(newVars)):
            newVars[i] += random.choice([-1, 1]) * 0.01
            newVars[i] = max(0, newVars[i])  # 確保變量非負

        # 計算新變量組合的目標函數值
        newValue = f(newVars)

        # 如果新變量組合的目標函數值更大，則更新變量和目標函數值
        if newValue > value:
            vars = newVars
            value = newValue
            print(f"Current best value: {value:.4f}, Variables: {vars}")
            fails = 0  # 重置失敗計數器
        else:
            fails += 1  # 增加失敗計數器

    # 輸出最終結果
    print(f"Final best value: {value:.4f}, Variables: {vars}")
