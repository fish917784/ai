import os
from groq import Groq

# 设置 Groq API 密钥
api_key = "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"

# 初始化 Groq 客户端
client = Groq(api_key=api_key)

# 尝试删除旧的输出文件
try:
    os.remove('./chat.md')
    print('Old output file removed.')
except FileNotFoundError:
    pass
except Exception as e:
    print(f'Error while removing file: {e}')

# 可用的语言模型列表
models = ['llama3-70b-8192', 'llama3-8b-8192', 'mixtral-8x7b-32768']

# 打印模型选择菜单
print("----- Choose model -----")
print("[1] llama3-70b-8192")
print("[2] llama3-8b-8192 (default)")
print("[3] mixtral-8x7b-32768")

# 用户选择模型
choice = input("Pick a model (default: 2): ").strip()
if choice not in ["1", "2", "3"]:
    print("Invalid value, using default (llama3-8b-8192).")
    choice = '2'

# 确定选择的模型
model_type = models[int(choice) - 1]

# 初始化问题
question = "Hello!"

# 进入交互循环
while question.lower() != "exit":
    # 生成对话回复
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": question}],
        model=model_type
    )

    # 将对话内容写入文件
    with open('chat.md', 'a', encoding='UTF-8') as f:
        f.write(f"## Prompt:\n{question}\n\n"
                f"## Response:\n{chat_completion.choices[0].message.content}\n\n")

    # 打印对话回复
    print(f"\n{chat_completion.choices[0].message.content}\n")

    # 提示用户输入下一个问题或退出
    question = input("Prompt (type 'exit' to exit): ").strip()

