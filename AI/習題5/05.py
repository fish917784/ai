from micrograd.engine import Value
import random

# 定義一個簡單的全連接神經網絡
class Neuron:
    def __init__(self, nin):
        self.w = [Value(random.uniform(-1,1)) for _ in range(nin)]
        self.b = Value(0)
    
    def __call__(self, x):
        act = sum((wi*xi for wi, xi in zip(self.w, x)), self.b)
        out = act.tanh()
        return out
    
    def parameters(self):
        return self.w + [self.b]

class Layer:
    def __init__(self, nin, nout):
        self.neurons = [Neuron(nin) for _ in range(nout)]
    
    def __call__(self, x):
        outs = [n(x) for n in self.neurons]
        return outs
    
    def parameters(self):
        return [p for neuron in self.neurons for p in neuron.parameters()]

class MLP:
    def __init__(self, nin, nouts):
        sz = [nin] + nouts
        self.layers = [Layer(sz[i], sz[i+1]) for i in range(len(sz)-1)]
    
    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x
    
    def parameters(self):
        return [p for layer in self.layers for p in layer.parameters()]

# 示例數據
xs = [[2.0, 3.0], [3.0, -1.0], [4.0, 2.0], [1.0, 1.0]]
ys = [1.0, -1.0, 1.0, -1.0]  # 實際標籤

# 創建一個2-2-1的神經網絡
n = MLP(2, [2, 1])

# 訓練網絡
for k in range(100):
    # 正向傳播
    ypred = [n(x) for x in xs]
    loss = sum((yout[0] - y)**2 for yout, y in zip(ypred, ys))
    
    # 反向傳播
    for p in n.parameters():
        p.grad = 0.0
    loss.backward()
    
    # 更新權重
    for p in n.parameters():
        p.data -= 0.1 * p.grad
    
    print(k, loss.data)
