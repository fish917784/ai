#用chatgpt幫助解答
import random
import copy

# 課程資訊
courses = [
    {'teacher': '甲', 'name':'機率', 'hours': 2},
    {'teacher': '甲', 'name':'線代', 'hours': 3},
    {'teacher': '甲', 'name':'離散', 'hours': 3},
    {'teacher': '乙', 'name':'視窗', 'hours': 3},
    {'teacher': '乙', 'name':'科學', 'hours': 3},
    {'teacher': '乙', 'name':'系統', 'hours': 3},
    {'teacher': '乙', 'name':'計概', 'hours': 3},
    {'teacher': '丙', 'name':'軟工', 'hours': 3},
    {'teacher': '丙', 'name':'行動', 'hours': 3},
    {'teacher': '丙', 'name':'網路', 'hours': 3},
    {'teacher': '丁', 'name':'媒體', 'hours': 3},
    {'teacher': '丁', 'name':'工數', 'hours': 3},
    {'teacher': '丁', 'name':'動畫', 'hours': 3},
    {'teacher': '丁', 'name':'電子', 'hours': 4},
    {'teacher': '丁', 'name':'嵌入', 'hours': 3},
    {'teacher': '戊', 'name':'網站', 'hours': 3},
    {'teacher': '戊', 'name':'網頁', 'hours': 3},
    {'teacher': '戊', 'name':'演算', 'hours': 3},
    {'teacher': '戊', 'name':'結構', 'hours': 3},
    {'teacher': '戊', 'name':'智慧', 'hours': 3}
]

teachers = ['甲', '乙', '丙', '丁', '戊']
rooms = ['A', 'B']
slots = [
    'A11', 'A12', 'A13', 'A14', 'A15', 'A16', 'A17',
    'A21', 'A22', 'A23', 'A24', 'A25', 'A26', 'A27',
    'A31', 'A32', 'A33', 'A34', 'A35', 'A36', 'A37',
    'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A47',
    'A51', 'A52', 'A53', 'A54', 'A55', 'A56', 'A57',
    'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
    'B21', 'B22', 'B23', 'B24', 'B25', 'B26', 'B27',
    'B31', 'B32', 'B33', 'B34', 'B35', 'B36', 'B37',
    'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47',
    'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57'
]

class Schedule:
    def __init__(self):
        self.schedule = {slot: {'teacher': '', 'course': ''} for slot in slots}
        self.initialize_schedule()

    def initialize_schedule(self):
        for course in courses:
            hours = course['hours']
            while hours > 0:
                slot = random.choice(slots)
                if self.schedule[slot]['teacher'] == '':
                    self.schedule[slot] = {'teacher': course['teacher'], 'course': course['name']}
                    hours -= 1

    def evaluate(self):
        score = 0
        for slot, value in self.schedule.items():
            if value['teacher'] != '':
                score += 1
        return score

    def get_neighbors(self):
        neighbors = []
        for _ in range(100):
            neighbor = copy.deepcopy(self)
            slot1, slot2 = random.sample(slots, 2)
            neighbor.schedule[slot1], neighbor.schedule[slot2] = neighbor.schedule[slot2], neighbor.schedule[slot1]
            neighbors.append(neighbor)
        return neighbors

    def hill_climbing(self):
        current = self
        while True:
            neighbors = current.get_neighbors()
            next_eval = max(neighbors, key=lambda x: x.evaluate())
            if next_eval.evaluate() <= current.evaluate():
                break
            current = next_eval
        return current

    def display(self):
        for slot, value in sorted(self.schedule.items()):
            print(f"{slot}: {value['teacher']} - {value['course']}")

# 執行排課系統
initial_schedule = Schedule()
print("初始排課表:")
initial_schedule.display()

print("\n進行爬山演算法優化...")
optimized_schedule = initial_schedule.hill_climbing()

print("\n優化後排課表:")
optimized_schedule.display()
