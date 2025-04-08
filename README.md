# 摘要：Keras MNIST手寫數字辨識資料集處理指南

## 1. 環境設置與資料下載
### 1.1 啟動Jupyter Notebook
- **步驟**：
  1. 開啟命令提示字元（Win+R → 輸入`cmd`）
  2. 執行 `jupyter notebook`
  3. 透過瀏覽器開啟Notebook（預設URL含token驗證）

### 1.2 下載MNIST資料集
```python
from keras.datasets import mnist
(X_train_image, y_train_label), (X_test_image, y_test_label) = mnist.load_data()
```
* 儲存路徑：C:\Users\[使用者名稱]\.keras\datasets\mnist.npz
* 資料規模：
* 訓練資料：60,000筆（28x28影像 + 標籤）
* 測試資料：10,000筆

##  2. 資料探索與視覺化
###   2.1 資料結構
```
print(x_train_image.shape)  # (60000, 28, 28)
print(y_train_label.shape)  # (60000,)
```
###  2.2 單一影像顯示
* 自訂函數 plot_image() 顯示灰階影像


範例：第0筆影像為數字5，標籤驗證 y_train_label[0] 輸出 5）

### 2.3 多筆資料視覺化
* 函數 plot_images_labels_prediction() 顯示批次影像與標籤
```
plot_images_labels_prediction(x_train_image, y_train_label, [], 0, 10)
```
## 3. 資料預處理
### 3.1 特徵（Feature）處理
### Reshape + 標準化
```
# 轉換為1維向量（長度784）
x_Train = x_train_image.reshape(60000, 784).astype('float32')
x_Test = x_test_image.reshape(10000, 784).astype('float32')

# 像素值標準化（0-255 → 0-1）
x_Train_normalize = x_Train / 255
x_Test_normalize = x_Test / 255
```
* 驗證：x_Train_normalize[0] 輸出值介於0~1之間
### 3.2 標籤（Label）處理
### One-Hot Encoding
```
from keras.utils import np_utils
y_TrainOneHot = np_utils.to_categorical(y_train_label)
y_TestOneHot = np_utils.to_categorical(y_test_label)
```
* 轉換範例：數字 5 → [0,0,0,0,0,1,0,0,0,0]
* 驗證：y_TrainOneHot[:5] 輸出前5筆編碼結果
###  4. 關鍵程式碼片段
### 4.1 資料預處理流程

```
# 特徵處理
x_Train = x_train_image.reshape(60000, 784).astype('float32')
x_Train_normalize = x_Train / 255

# 標籤處理
y_TrainOneHot = np_utils.to_categorical(y_train_label)
```
### 4.2 視覺化工具函數
```
def plot_images_labels_prediction(images, labels, prediction, idx, num=10):
    plt.figure(figsize=(12, 14))
    for i in range(num):
        ax = plt.subplot(5, 5, i+1)
        ax.imshow(images[idx], cmap='binary')
        title = f"label={labels[idx]}"
        if len(prediction) > 0:
            title += f", predict={prediction[idx]}"
        ax.set_title(title, fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        idx += 1
    plt.show()
```
## 5. 總結

* 資料規格：60K訓練 + 10K測試，每筆為28x28灰階影像
* 預處理步驟：
* 特徵：Reshape為784維向量 + 標準化
* 標籤：One-Hot Encoding轉換